from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.exceptions import AirflowException
import pandas as pd
import os

# Configuration
GCS_BUCKET = 'citibike-data-stellar-mercury-455917-d9-dev'
GCS_PATH = 'processed_data/processed_citibike_data.parquet'  # Path in your bucket

def process_and_upload_citibike_data(**kwargs):
    try:
        input_path = "/opt/notebooks/merged_citibike_trips.csv"
        output_path = "/home/denis/data/processed_citibike_data.parquet"
        
        # 1. Process the data
        print(f"Loading data from {input_path}")
        df = pd.read_csv(input_path)
        
        # Your existing data processing logic here...
        
        print(f"Saving processed data to {output_path}")
        df.to_parquet(output_path, index=False)
        
        # 2. Upload to GCS
        print(f"Uploading to GCS: gs://{GCS_BUCKET}/{GCS_PATH}")
        gcs_hook = GCSHook(gcp_conn_id='google_cloud_default')
        gcs_hook.upload(
            bucket_name=GCS_BUCKET,
            object_name=GCS_PATH,
            filename=output_path,
            mime_type='application/parquet'
        )
        
        return f"Successfully uploaded to gs://{GCS_BUCKET}/{GCS_PATH}"
    except Exception as e:
        raise AirflowException(f"Data processing/upload failed: {str(e)}")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'process_citibike_data',
    default_args=default_args,
    description='Processes Citibike data and uploads to GCS',
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['citibike', 'data-processing', 'gcs'],
) as dag:

    install_deps = BashOperator(
        task_id='install_dependencies',
        bash_command='pip install --user geopy==2.3.0 pandas==1.3.5 pyarrow==8.0.0 apache-airflow-providers-google',
    )

    process_and_upload_task = PythonOperator(
        task_id='process_and_upload_citibike_data',
        python_callable=process_and_upload_citibike_data,
    )

    install_deps >> process_and_upload_task
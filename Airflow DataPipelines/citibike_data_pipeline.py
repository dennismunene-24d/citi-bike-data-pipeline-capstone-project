from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.exceptions import AirflowException
import os

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

def verify_downloads():
    data_dir = os.path.expanduser('~/data')
    required_files = [
        'JC-202401-citibike-tripdata.csv',
        'JC-202402-citibike-tripdata.csv',
        # Add all expected files here
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(os.path.join(data_dir, file)):
            missing_files.append(file)
    
    if missing_files:
        raise AirflowException(f"Missing files: {', '.join(missing_files)}")
    print("All files downloaded successfully!")

with DAG(
    'citibike_data_pipeline',
    default_args=default_args,
    description='Downloads and processes Citibike trip data',
    schedule_interval='@monthly',  # Runs at the beginning of each month
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['citibike', 'data'],
) as dag:

    download_task = BashOperator(
        task_id='download_and_extract_data',
        bash_command='/opt/airflow/dags/scripts/download.sh',
        env={
            'HOME': '/home/airflow',  # Override $HOME to ensure consistent path
        },
    )

    verify_task = PythonOperator(
        task_id='verify_downloads',
        python_callable=verify_downloads,
    )

    # Add a cleanup task if needed
    cleanup_task = BashOperator(
        task_id='cleanup_temp_files',
        bash_command='rm -f /home/airflow/data/*.zip',  # Cleanup zip files
        trigger_rule='all_done',  # Runs regardless of success/failure
    )

    download_task >> verify_task >> cleanup_task
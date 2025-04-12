from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.exceptions import AirflowException
import os
import pandas as pd


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

def merge_csv_files(**kwargs):
    input_dir = "/data"  
    output_file = "/opt/notebooks/merged_citibike_trips.csv"
    
    try:
        # Get list of CSV files
        csv_files = [f for f in os.listdir(input_dir) 
                    if f.endswith('.csv') and not f.startswith('._')]
        
        if not csv_files:
            raise AirflowException("No CSV files found in input directory")
        
        print(f"Found {len(csv_files)} CSV files to merge...")
        
        # Process files with error handling
        chunks = []
        failed_files = []
        
        for file in tqdm(sorted(csv_files), desc="Merging files"):
            filepath = os.path.join(input_dir, file)
            try:
                df = pd.read_csv(filepath)
                chunks.append(df)
            except Exception as e:
                failed_files.append(file)
                print(f"Warning: Error processing {file}: {str(e)}")
                continue
        
        if not chunks:
            raise AirflowException("No files were processed successfully")
        
        # Merge and save
        final_df = pd.concat(chunks, ignore_index=True)
        final_df.to_csv(output_file, index=False)
        
        # Push results to XCom for downstream tasks
        kwargs['ti'].xcom_push(key='merged_file', value=output_file)
        kwargs['ti'].xcom_push(key='record_count', value=len(final_df))
        
        print(f"\nSuccessfully merged {len(chunks)}/{len(csv_files)} files")
        print(f"Failed to process: {failed_files}")
        print(f"Final shape: {final_df.shape}")
        
    except Exception as e:
        raise AirflowException(f"Merge failed: {str(e)}")

with DAG(
    'merge_citibike_data',
    default_args=default_args,
    description='Merges monthly Citibike trip CSVs into single file',
    schedule_interval=None,  # Manual trigger or downstream from download DAG
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['citibike', 'data-processing'],
) as dag:

    merge_task = PythonOperator(
        task_id='merge_csv_files',
        python_callable=merge_csv_files,
        provide_context=True,
    )

    # Add data validation task example
    validate_task = PythonOperator(
        task_id='validate_merged_data',
        python_callable=lambda **context: print(
            f"Validating {context['ti'].xcom_pull(key='record_count')} records"
        ),
    )

    merge_task >> validate_task
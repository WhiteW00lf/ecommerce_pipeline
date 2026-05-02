from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime,timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'ecommerce_pipeline',
    default_args=default_args,
    description='A simple e-commerce data pipeline',
    schedule='0 6 * * *',
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:
    generate = BashOperator(
        task_id='generate and load data',
        bash_command='python3 /home/ubuntu/ecommerce_pipeline/extract/generate.py'
    )
    

    dbt_run = BashOperator(
        task_id='dbt run',
        bash_command='cd /home/ubuntu/ecommerce_pipeline/ecommercepipeline && dbt run',
    )

    dbt_test = BashOperator(
        task_id='dbt test',
        bash_command='cd /home/ubuntu/ecommerce_pipeline/ecommercepipeline && dbt test',
    )

    generate >> dbt_run >> dbt_test 
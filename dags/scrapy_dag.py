from airflow import DAG
from datetime import datetime

from airflow.operators.bash import BashOperator

with DAG('scrapy_dag', start_date=datetime(2024, 1, 2), schedule_interval='30 * * * *', catchup=False) as dag :
    scrapy_task = BashOperator(
        task_id='scrapy_task',
        bash_command='cd ../../opt/airflow/dags/magalu_scraper && scrapy crawl magalu_book -O ../magalu_book.json'
    )

    success_task = BashOperator(
        task_id='success_task',
        bash_command='echo "Success!"'
    )

    scrapy_task >> success_task
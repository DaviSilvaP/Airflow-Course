from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime

default_args = {
    'start_date': datetime(2020, 1, 1)
}

with DAG('parallel_dag', schedule_interval='@daily',
         default_args=default_args, catchup=False) as dag:

    bash_task1 = BashOperator(
        task_id='bash_task1',
        bash_command='sleep 3'
    )

    bash_task2 = BashOperator(
        task_id='bash_task2',
        bash_command='sleep 3'
    )

    bash_task3 = BashOperator(
        task_id='bash_task3',
        bash_command='sleep 3'
    )

    bash_task4 = BashOperator(
        task_id='bash_task4',
        bash_command='sleep 3'
    )

    bash_task1 >> [bash_task2, bash_task3] >> bash_task4

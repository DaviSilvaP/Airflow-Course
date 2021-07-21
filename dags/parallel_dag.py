from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup

from datetime import datetime

default_args = {
    'start_date': datetime(2020, 1, 1)
}

with DAG('parallel_dag', schedule_interval='@daily',
         default_args=default_args, concurrency=16,
         max_active_runs=16, catchup=False) as dag:

    bash_task1 = BashOperator(
        task_id='bash_task1',
        bash_command='sleep 3'
    )

    with TaskGroup('processing_tasks') as processing_tasks:
        bash_task2 = BashOperator(
            task_id='bash_task2',
            bash_command='sleep 3'
        )

        # Quando usando em grupos, a task_id vai ser ligada com o nome do grupo
        # No fim, será task_id = spark_tasks.bash_task3
        with TaskGroup('spark_tasks') as spark_tasks:
            bash_task3 = BashOperator(
                task_id='bash_task3',
                bash_command='sleep 3'
            )

        with TaskGroup('flink_tasks') as flink_tasks:
            bash_task3 = BashOperator(
                task_id='bash_task3',
                bash_command='sleep 3'
            )

    bash_task4 = BashOperator(
        task_id='bash_task4',
        bash_command='sleep 3'
    )

    bash_task1 >> processing_tasks >> bash_task4

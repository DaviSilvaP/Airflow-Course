from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator

from datetime import datetime
from subdags.subdag_parallel_dag import subgdag_parallel_dag


default_args = {
    'start_date': datetime(2020, 1, 1)
}

with DAG('parallel_dag_v2', schedule_interval='@daily',
         default_args=default_args, concurrency=16,
         max_active_runs=16, catchup=False) as dag:

    bash_task1 = BashOperator(
        task_id='bash_task1',
        bash_command='sleep 3'
    )

    # child_dag_id will be the same as the task_id
    processing = SubDagOperator(
        task_id='processing_tasks',
        subdag=subgdag_parallel_dag('parallel_dag_v2', 'processing_tasks',
                                    default_args)
    )

    bash_task4 = BashOperator(
        task_id='bash_task4',
        bash_command='sleep 3'
    )

    bash_task1 >> processing >> bash_task4

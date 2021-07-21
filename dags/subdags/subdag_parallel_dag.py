from airflow import DAG
from airflow.operators.bash import BashOperator


def subgdag_parallel_dag(parent_dag_id, child_dag_id, default_args):
    with DAG(dag_id=f'{parent_dag_id}.{child_dag_id}',
             default_args=default_args) as dag:

        bash_task2 = BashOperator(
            task_id='bash_task2',
            bash_command='sleep 3'
        )

        bash_task3 = BashOperator(
            task_id='bash_task3',
            bash_command='sleep 3'
        )

        return dag

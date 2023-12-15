from datetime import datetime
import random

from airflow import DAG
from airflow.decorators import task

with DAG(
        dag_id='python_operator_example',
        start_date=datetime(2023, 9, 25),
) as dag:
    @task(task_id="print_to_logs")
    def print_to_logs(ds=None, **kwargs):
        """Print the Airflow context and ds variable from the context."""
        print(kwargs)
        print(ds)
        return "Whatever you return gets printed in the logs"

    print_context = print_to_logs()

    @task(task_id="random_number")
    def random_number():
        n = random.randint(0, 10000)
        return print(n)

    random_number = random_number()

    print_context >> random_number

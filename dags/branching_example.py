"""Example DAG demonstrating the usage of the `@task.branch`
TaskFlow API decorator."""

from airflow.decorators import dag, task
from airflow.operators.empty import EmptyOperator
from airflow.utils.edgemodifier import Label

import random
from pendulum import datetime


@dag(
    start_date=datetime(2023, 1, 1),
    catchup=False,
    schedule="@daily"
)
def branch_python_operator_decorator_example():

    run_this_first = EmptyOperator(task_id="run_this_first")

    options = ["branch_a", "branch_b", "branch_c", "branch_d"]

    @task.branch(task_id="branching")
    def random_choice(choices):
        return random.choice(choices)

    random_choice_instance = random_choice(choices=options)

    run_this_first >> random_choice_instance

    join = EmptyOperator(
        task_id="join",
        trigger_rule="none_failed_min_one_success"
    )

    for option in options:

        t = EmptyOperator(
            task_id=option
        )

        empty_follow = EmptyOperator(
            task_id="follow_" + option
        )

        # Label is optional here, but it can help identify more complex branches
        random_choice_instance >> Label(option) >> t >> empty_follow >> join


branch_python_operator_decorator_example()
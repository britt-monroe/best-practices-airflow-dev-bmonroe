from datetime import datetime
from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator

from modules.slack_notify import task_fail_slack_alert

default_args = {
    "on_failure_callback": task_fail_slack_alert,
}

with DAG(
        dag_id='mysql_operator_example',
        start_date=datetime(2023, 9, 25),
        default_args=default_args,
) as dag:
    create_view = MySqlOperator(
        task_id='create_view',
        mysql_conn_id='mysql_conn',
        sql="""CREATE VIEW airflow_best_practices.vw_mega_millions_multiplier AS
                SELECT
                *
                FROM airflow_best_practices.mega_millions_winning_numbers
                WHERE Multiplier = 3""",
    )

    create_view

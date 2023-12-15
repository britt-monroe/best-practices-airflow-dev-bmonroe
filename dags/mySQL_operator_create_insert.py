from datetime import datetime
from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator

default_args = {
    "owner": "data eng team",
    "retries": 0,
}

with DAG(
        dag_id='mysql_operator_example_two_step',
        start_date=datetime(2023, 9, 25),
        default_args=default_args,
) as dag:
    create_table = MySqlOperator(
        task_id='create_table',
        mysql_conn_id='mysql_conn',
        sql="sql/create_table.sql",
    )

    insert_data = MySqlOperator(
        task_id='insert_data',
        mysql_conn_id='mysql_conn',
        sql="sql/insert_table.sql",
    )

    create_table >> insert_data
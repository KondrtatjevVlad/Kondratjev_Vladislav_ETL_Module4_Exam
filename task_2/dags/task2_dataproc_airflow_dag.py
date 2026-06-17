from datetime import datetime

from airflow import DAG
from airflow.utils.trigger_rule import TriggerRule

from airflow.providers.yandex.operators.yandexcloud_dataproc import (
    DataprocCreateClusterOperator,
    DataprocCreatePysparkJobOperator,
    DataprocDeleteClusterOperator,
)


FOLDER_ID = "b1gtbeuc1thn2lkp2k9q"
ZONE = "ru-central1-b"

BUCKET = "etl-exam-vladislav-transactions-20260615-01"

SUBNET_ID = "e2lk2srnjm4v6c616s3p"
SERVICE_ACCOUNT_ID = "aje41u1agre3fumu8qtr"
SECURITY_GROUP_ID = "enpbkt213m71ogc6m7f9"

SSH_PUBLIC_KEY = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPmb7264ybsFUT16MXuGt93vNrf82c0r6fW3exYSrOHA dataproc-airflow"

INPUT_PATH = f"s3a://{BUCKET}/task_2/input/applications_v2.csv"
PYSPARK_SCRIPT = f"s3a://{BUCKET}/task_2/pyspark/process_applications.py"
OUTPUT_PATH = f"s3a://{BUCKET}/task_2/output/applications_summary"


with DAG(
    dag_id="task2_dataproc_airflow_dag",
    start_date=datetime(2026, 6, 16),
    schedule=None,
    catchup=False,
    tags=["exam", "task_2", "dataproc", "pyspark"],
) as dag:

    create_cluster = DataprocCreateClusterOperator(
        task_id="create_dataproc_cluster",
        folder_id=FOLDER_ID,
        cluster_name="task2-dataproc-cluster",
        cluster_description="Temporary cluster for ETL exam task 2",
        cluster_image_version="2.1",
        zone=ZONE,
        subnet_id=SUBNET_ID,
        service_account_id=SERVICE_ACCOUNT_ID,
        security_group_ids=[SECURITY_GROUP_ID],
        ssh_public_keys=[SSH_PUBLIC_KEY],
        s3_bucket=BUCKET,
        services=["HDFS", "YARN", "SPARK"],
        masternode_resource_preset="s2.small",
        masternode_disk_type="network-hdd",
        masternode_disk_size=32,
        datanode_count=1,
        datanode_resource_preset="s2.small",
        datanode_disk_type="network-hdd",
        datanode_disk_size=32,
        computenode_count=0,
        properties={
            "spark:spark.submit.deployMode": "cluster",
            "dataproc:disable_cloud_logging": "false",
        },
    )

    run_pyspark_job = DataprocCreatePysparkJobOperator(
        task_id="run_pyspark_job",
        cluster_id=create_cluster.output,
        main_python_file_uri=PYSPARK_SCRIPT,
        args=[
            "--input",
            INPUT_PATH,
            "--output",
            OUTPUT_PATH,
        ],
        properties={
            "spark.submit.deployMode": "cluster",
        },
        name="task2-applications-processing",
    )

    delete_cluster = DataprocDeleteClusterOperator(
        task_id="delete_dataproc_cluster",
        cluster_id=create_cluster.output,
        trigger_rule=TriggerRule.ALL_DONE,
    )

    create_cluster >> run_pyspark_job >> delete_cluster
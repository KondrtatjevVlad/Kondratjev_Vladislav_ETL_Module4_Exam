from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import argparse


def main(input_path: str, output_path: str) -> None:
    spark = (
        SparkSession.builder
        .appName("task2_applications_processing")
        .getOrCreate()
    )

    df = (
        spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .csv(input_path)
    )

    cleaned = (
        df
        .withColumn("requested_amount", F.col("requested_amount").cast("double"))
        .withColumn("approved_amount", F.col("approved_amount").cast("double"))
        .withColumn("credit_score", F.col("credit_score").cast("int"))
        .withColumn("processing_time_sec", F.col("processing_time_sec").cast("int"))
        .withColumn("event_date", F.to_date("event_time"))
    )

    summary = (
        cleaned
        .groupBy("event_date", "region_code", "product_type", "decision_status")
        .agg(
            F.count("*").alias("applications_cnt"),
            F.sum("requested_amount").alias("requested_amount_sum"),
            F.sum("approved_amount").alias("approved_amount_sum"),
            F.avg("credit_score").alias("avg_credit_score"),
            F.avg("processing_time_sec").alias("avg_processing_time_sec")
        )
        .orderBy("event_date", "region_code", "product_type", "decision_status")
    )

    summary.write.mode("overwrite").parquet(output_path)

    spark.stop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    main(args.input, args.output)
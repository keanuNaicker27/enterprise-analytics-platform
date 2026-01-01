import sys
from awsglue.transforms import *
from pyspark.context import SparkContext
from awsglue.context import GlueContext

glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session

# Load from S3
input_df = spark.read.json("s3://enterprise-data-lake-raw/raw_events/")

input_df.createOrReplaceTempView("raw_events")

# Flattening the nested JSON context in Spark
transformed_df = spark.sql("""
    SELECT 
        event_id,
        timestamp as event_time,
        user_id,
        event_type,
        context.source as source_system,
        context.ip as ip_address
    FROM raw_events
""")

# Write to Parquet (Optimized for Redshift Spectrum/BigQuery Omni)
transformed_df.write.mode("overwrite").parquet("s3://enterprise-data-lake-raw/processed_data/")

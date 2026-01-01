import sys
from awsglue.transforms import *
from pyspark.context import SparkContext
from awsglue.context import GlueContext

glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session

# Load from S3
input_df = spark.read.json("s3://enterprise-data-lake-raw/raw_events/")

# Staff Level: Using Spark SQL for complex transformations
input_df.createOrReplaceTempView("raw_events")

transformed_df = spark.sql("""
    SELECT 
        event_id,
        CAST(timestamp AS TIMESTAMP) as event_time,
        user_id,
        UPPER(event_type) as event_name
    FROM raw_events
    WHERE event_id IS NOT NULL
""")

# Write to Parquet (Optimized for Redshift Spectrum/BigQuery Omni)
transformed_df.write.mode("overwrite").parquet("s3://enterprise-data-lake-raw/processed_data/")

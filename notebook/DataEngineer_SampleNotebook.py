# Databricks notebook source

# Databricks Notebook Example: Silver and Gold Data Processing

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count, min, max, to_timestamp

# Initialize Spark Session
spark = SparkSession.builder.appName("SilverGoldPipeline").getOrCreate()

# COMMAND ----------

# Create the Bronze schema if it doesn't exist
spark.sql("CREATE SCHEMA IF NOT EXISTS bronze")

# Step 1: Create Bronze Table (Raw Data)
bronze_data = [
    ("TXN123", "CUST001", "2024-02-10T12:34:56Z", "100.5", "USD", "Completed"),
    ("TXN124", "CUST002", "2024-02-11T14:20:10Z", "250.0", "USD", "Pending"),
    ("TXN125", "CUST001", "2024-02-12T16:45:30Z", "300.0", "USD", "Completed"),
]

bronze_columns = [
    "transaction_id",
    "customer_id",
    "transaction_date",
    "amount",
    "currency",
    "payment_status",
]
bronze_df = spark.createDataFrame(bronze_data, bronze_columns)

# Write to Delta Bronze Table
bronze_df.write.format("delta").mode("overwrite").saveAsTable("bronze.transactions")

# COMMAND ----------

spark.sql("CREATE SCHEMA IF NOT EXISTS silver")

# Step 2: Create Silver Table (Cleaned & Structured Data)
silver_df = spark.sql(
    """
    SELECT
        transaction_id,
        customer_id,
        to_timestamp(transaction_date, 'yyyy-MM-dd"T"HH:mm:ssX') AS transaction_timestamp,
        CAST(amount AS DECIMAL(10,2)) AS amount,
        currency,
        payment_status
    FROM bronze.transactions
    WHERE payment_status = 'Completed'
    """
)

# Write to Delta Silver Table
silver_df.write.format("delta").mode("overwrite").saveAsTable("silver.transactions")

# COMMAND ----------

spark.sql("CREATE SCHEMA IF NOT EXISTS gold")

# Step 3: Create Gold Table (Aggregated Data for Reporting)
gold_df = silver_df.groupBy("customer_id").agg(
    sum("amount").alias("total_spent"),
    count("transaction_id").alias("transaction_count"),
    min("transaction_timestamp").alias("first_purchase"),
    max("transaction_timestamp").alias("last_purchase"),
)

# Write to Delta Gold Table
gold_df.write.format("delta").mode("overwrite").saveAsTable("gold.customer_spending")

# COMMAND ----------

# Display Gold Data
display(gold_df)

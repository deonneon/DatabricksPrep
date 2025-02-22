# Apps

## DBFS

Designed to be for temporary files

The real data should be hosted in the cloud env.

It is not optimized for large file distributed storage and can suffer from latency and performance issues.

## Hosting

### Cloud Objects

Mount cloud providers to /mnt for easy access

AWS S3

Azure Data Lake Storage (ADLS)

Google Cloud Storage (GCS)

#### Cloud Delta Lake

Delta table is commonly mounted at

/mnt/delta

### Onprem Objects

Can be used for onprem storage through NFS hosting.

Can connect to HDFS of the Hadoop platform.

#### Onprem DB/Hive

If on-prem storage is a database (Hive, PostgreSQL, MySQL, Oracle, SQL Server), use JDBC/ODBC connectors to access the database.

## Photon

An optimized custom CPU query engine made by Databricks
It sits underneath Databricks SQL and acts as an alternative to Spark's execution engine.
It can support other processes beside Databricks SQL as the engine
It is meant more for Data Engineering that ML so SQL heavy compute or Delta Lake compute.
Photon accelerates vectorized cpu operations like CUDA does for gpu tensors.
CUDA is like photon and spark combined actually.
Photon is intranode while Spark is distrbuted.

## Delta Live Table

A pipeline from ingestion to Delta Lakehouse

Can be used in place of Kafka.

If you can tolerate some data loss: Direct ingestion
If you need guaranteed delivery: Kafka provides better guarantees

Kafka is decoupling of data producers and consumers
DLT - Direct ingestion using Databricks Auto Loader

DLT cannot write to external tables

Structured Streaming is the processing engine of DLT

```sql
-- Write to DLT
CREATE OR REFRESH LIVE TABLE bronze_transactions
AS SELECT * FROM bronze_df
```

## CDC

Change data capture is used to track deltas.

You can connect kafka to DLT for CDC for streaming
You can connect kafka to AutoLoader for CDC for batch

You will still need Qlik or DMS upstream to track the changes.

## Lakehouse

The pillars “Data and AI Governance” and “Interoperability and Usability” cover concerns specific to the lakehouse.

## Unity Catalog

Data linearage, Delta Sharing, Data Governance

Can be exported to Enterprise Data Governance lie CollibraDQ

## Autoloader

Autoloader can be called using spark.readStream.format("cloudFiles")

AutoLoader only works with structuredStreaming so readStream is required and not read.

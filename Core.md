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

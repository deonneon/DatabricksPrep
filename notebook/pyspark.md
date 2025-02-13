# Pyspark

Fundamentals

## Attach a cluster and Stop a Cluster when Done

## Import Library

You do not need to import pyspark or set a sparksession.

```py
%pip install package-name
```

for custom jars

```py
spark.sparkContext.addPyFile("dbfs:/FileStore/jars/custom.jar")
```

## Define Config

Set at top of notebook

```py
spark.conf.set("spark.sql.shuffle.partitions", "200")
```

## Read and Write data

```py
# from DBFS
df = spark.read.format("delta").load("dbfs:/mnt/data/sample_table")

# from DB SQL
df = spark.sql("SELECT * FROM my_database.my_table")

# to DBFS
df.write.format("delta").mode("overwrite").save("dbfs:/mnt/data/output_table")
```

SQL update only work for delta tables.

```py
spark.sql("""
    UPDATE customers
    SET status = 'inactive'
    WHERE customer_id = 101
""")
```

need to convert

```py
# only for parquet tables
spark.sql("CONVERT TO DELTA my_database.my_table;")

# else (e.g., CSV, JSON, or Hive-managed table) create a new Delta table and migrate your data:
df = spark.read.format("csv").option("header", "true").load("dbfs:/mnt/data/my_table")
df.write.format("delta").mode("overwrite").saveAsTable("my_database.my_table")
```

## Display data

```py
display(df)
```

list dir

dbutils

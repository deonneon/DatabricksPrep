# df

## common df operation

```py
# filter
df.filter( condition )

# write to delta live table
df.write.format("delta").mode("overwrite").save(delta_table_path)

```

| Operation   | Pandas                          | PySpark                                                   |
| ----------- | ------------------------------- | --------------------------------------------------------- |
| Read CSV    | pd.read_csv("file.csv")         | spark.read.csv("file.csv", header=True, inferSchema=True) |
| Filtering   | df[df["amount"] > 100]          | df.filter(df.amount > 100)                                |
| Aggregation | df.groupby("customer_id").sum() | df.groupBy("customer_id").sum()                           |
| Joining     | pd.merge(df1, df2, on="id")     | df1.join(df2, "id")                                       |

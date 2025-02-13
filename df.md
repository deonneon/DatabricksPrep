# df

## common df operation

```py
# filter
df.filter( condition )

# write to delta live table
df.write.format("delta").mode("overwrite").save(delta_table_path)

```

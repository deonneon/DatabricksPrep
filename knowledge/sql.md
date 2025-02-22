# SQL

```sql
-- Display
SELECT * from catalog.table

-- Filter
SELECT * FROM catalog.table where column = 'columnName'

-- Create a table
CREATE TABLE IF NOT EXISTS bronze (
    id INT,
    emplid STRING
) USING DELTA

-- Insert data record
INSERT INTO bronze (
    id,
    emplid
) VALUES (1,'1DASDS')

-- Joining table
SELECT a.*, b.columnA
FROM tableA as a
JOIN tableB as b ON a.columnA = b.columnb
```

Post schema creation operation does not require type declaration

When doing alias, use lowercase to be proper.
tables should be lowercase

Default JOIN is inner join
LEFT JOIN tableB as b ON a.columnA = b.columnb
RIGHT JOIN tableB as b ON a.columnA = b.columnb

## SCHEMA commands

```sql
-- Create schema
CREATE SCHEMA IF NOT EXISTS my_schema;

-- Drop schema
DROP SCHEMA IF EXISTS my_schema CASCADE;

-- Alter schema
ALTER SCHEMA my_schema RENAME TO new_schema;

-- Show schema
SHOW SCHEMAS;

-- Use schema
USE my_schema;

```

cascade is like -r on rm -r which remove child dependencies

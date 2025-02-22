# to learn

## RDD

## RDBMS

Fancy world for relationship table.

Relational Database Management System
R(DB)MS

### Primary keys

A Primary Key is a column (or a combination of columns) that uniquely identifies each row in a table.

Characteristics of a Primary Key:
Unique: No two rows can have the same primary key value.
Not Null: A primary key column cannot have NULL values.
Single or Composite: It can be a single column or a combination of multiple columns (called a Composite Key).

### Foreign keys

Allows linking between the table. References a primary key in another table.

Primary and Foreign keys can be the same. This happens in 1-to-1 relationship table.

```sql
-- 1 to 1 example
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(100),
    Department VARCHAR(50)
);

CREATE TABLE EmployeeDetails (
    EmployeeID INT PRIMARY KEY,  -- Primary Key
    Address VARCHAR(255),
    PhoneNumber VARCHAR(15),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)  -- Foreign Key
);
```

## Schema evolution

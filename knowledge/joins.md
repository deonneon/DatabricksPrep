# Joins

There are many types of joins

1. Inner join
2. Left join
3. Right join
4. Self join
5. Cros join
6. Anti-left join
7. Anti-right join

## Inner join

Returns only the inner row that match with on foreign key

- All the columns will be returned
- Only non-matching rows will be omitted

## Left join

Returns all row from left.
Right table columns are added and filled only were there is matching

When there is no match, columns from the right are all returned but with nulls. There is no error that says nothing was found. This is by design to prevent the engine from crashes.

## Right join

Same as left but for the right table.

## Full join

Return all rows from both tables.
Nonmatching cases with have nulls in their respective columns

## Self join

Join table to itself but usually matching two different columns for the same key

example is a directroy with employeeID and managerID. An employee can be a manager so you get

| EmployeeID | Name          | ManagerID |
| ---------- | ------------- | --------- |
| 1          | Alice Johnson | NULL      |
| 2          | Bob Smith     | 1         |
| 3          | Carol Brown   | 1         |
| 4          | David Wilson  | 2         |
| 5          | Eva Davis     | 3         |

```sql
SELECT
    E.EmployeeID,
    E.Name         AS EmployeeName,
    M.EmployeeID   AS ManagerID,
    M.Name         AS ManagerName
FROM Employees AS E
LEFT JOIN Employees AS M
    ON E.ManagerID = M.EmployeeID;
```

Expected Outcome:

| EmployeeID | EmployeeName  | ManagerID | ManagerName   |
| ---------- | ------------- | --------- | ------------- |
| 1          | Alice Johnson | NULL      | NULL          |
| 2          | Bob Smith     | 1         | Alice Johnson |
| 3          | Carol Brown   | 1         | Alice Johnson |
| 4          | David Wilson  | 2         | Bob Smith     |
| 5          | Eva Davis     | 3         | Carol Brown   |

## Cross join

Generally doing a dot product to get all the possible combination from both tables

There is no ON clause

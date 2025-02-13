# Structured Dataset

If you're working with structured data that you may analyze later, converting it into a Pandas DataFrame or using List of Dictionaries would be the best approach.

```py
# list of tuples
data = [
    ("TXN123", "CUST001", "2024-02-10T12:34:56Z", "100.5", "USD", "Completed"),
    ("TXN124", "CUST002", "2024-02-11T14:20:10Z", "250.0", "USD", "Pending"),
]

# list of dictionary
data = [
    {"transaction_id": "TXN123", "customer_id": "CUST001", "transaction_date": "2024-02-10T12:34:56Z",
     "amount": "100.5", "currency": "USD", "payment_status": "Completed"},
    {"transaction_id": "TXN124", "customer_id": "CUST002", "transaction_date": "2024-02-11T14:20:10Z",
     "amount": "250.0", "currency": "USD", "payment_status": "Pending"},
]


# dataframe
import pandas as pd

data = [
    ("TXN123", "CUST001", "2024-02-10T12:34:56Z", 100.5, "USD", "Completed"),
    ("TXN124", "CUST002", "2024-02-11T14:20:10Z", 250.0, "USD", "Pending"),
]

columns = ["transaction_id", "customer_id", "transaction_date", "amount", "currency", "payment_status"]
df = pd.DataFrame(data, columns=columns)
print(df)

# names tuples

from collections import namedtuple

Transaction = namedtuple("Transaction", ["transaction_id", "customer_id", "transaction_date", "amount", "currency", "payment_status"])

data = [
    Transaction("TXN123", "CUST001", "2024-02-10T12:34:56Z", "100.5", "USD", "Completed"),
    Transaction("TXN124", "CUST002", "2024-02-11T14:20:10Z", "250.0", "USD", "Pending"),
]

print(data[0].transaction_id)  # Access like an object

# dataclass objects

from dataclasses import dataclass

@dataclass
class Transaction:
    transaction_id: str
    customer_id: str
    transaction_date: str
    amount: float
    currency: str
    payment_status: str

data = [
    Transaction("TXN123", "CUST001", "2024-02-10T12:34:56Z", 100.5, "USD", "Completed"),
    Transaction("TXN124", "CUST002", "2024-02-11T14:20:10Z", 250.0, "USD", "Pending"),
]

print(data[0].transaction_id)  # Access like an object

```

## Tradeoffs

**list of tuples**

Pros: Simple, works well for small datasets, tuples are immutable (ensuring data integrity).
Cons: Not as easy to manipulate as dictionaries or Pandas DataFrames.

**list of dictionary**

Pros: More readable, easier to manipulate, better compatibility with JSON and APIs.
Cons: Slightly more memory usage compared to tuples.

**dataframes**

Pros: Provides powerful data manipulation capabilities, built-in functions for filtering, aggregation, and transformation.
Cons: Requires pandas library, slightly more memory overhead.

**names tuples**

Pros: More readable than plain tuples, still immutable, slightly better performance than dictionaries.
Cons: Less flexible than dictionaries for dynamic keys.

**dataclass objects**

Pros: Provides structure, type hints, and better code organization.
Cons: Requires defining a class, slightly more setup.

## use cases

Which One Should You Use?

- For quick scripting or small datasets → List of tuples
- For JSON APIs or structured data → List of dictionaries
- For data science, analytics, or databases → Pandas DataFrame
- For performance-focused structured data → Named Tuples
- For clean object-oriented design → Dataclass

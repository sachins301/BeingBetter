"""
Generate Nested SQL Queries: Write a Python function that generates a nested SQL query based on multiple input conditions and filters.
"""

def generate_nested_sql(table, conditions):
    query = f"select * from {table} where "
    condition = " and ".join(f"{k} = {"'"+v+"'" if isinstance(v, str) else v}" for k, v in conditions.items())
    return query + condition


conditions = {"age": 30, "country": "USA"}
print(generate_nested_sql("users", conditions))
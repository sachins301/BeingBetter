"""
Dynamic Data Filtering: 
Write a function that accepts a set of filter conditions (in JSON) and dynamically filters a large dataset based on these conditions.
"""

def filter_data(data, filters):
    res = []
    return [item for item in data if all(item[k] == v for k, v in filters.items())]



data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]
filters = {"name": "Alice"}
print(filter_data(data, filters))
"""
Filter and Process Nested Lists: 
Given a list of nested lists or dictionaries, write a function that filters and processes the data to return key information based on user input.
"""

def filter_data(data, key, value):
    return [item for item in data if item[key] == value]


data = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Alice", "age": 35}]
print(filter_data(data, "name", "Alice"))
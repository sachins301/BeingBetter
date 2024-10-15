"""
Handle Missing Data in Nested Structures: 
Given a JSON-like structure with missing fields, write a function that safely processes it and fills in the missing values with defaults.
"""

def process_data(data):
    keys = set()
    for item in data:
        keys.update(item.keys())
    for item in data:
        item_keys = item.keys()
        for k in keys:
            if k not in item_keys:
                item[k] = 0
    return data


data = [{"name": "Alice"}, {"name": "Bob", "age": 30}]
print(process_data(data))
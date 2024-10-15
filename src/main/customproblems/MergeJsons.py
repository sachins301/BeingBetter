"""
Merge Multiple JSON Structures: 
Given two or more JSON-like data structures, write a function that merges them into a single structure, ensuring no duplicate keys.
"""

def merge_data(data1, data2):
    # data1.update(data2)

    return {**data1, **data2}

data1 = {"name": "Alice", "age": 25}
data2 = {"country": "USA"}
print(merge_data(data1, data2))
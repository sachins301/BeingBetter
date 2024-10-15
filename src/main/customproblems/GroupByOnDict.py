"""
Transform a List of Dictionaries: 
Given a list of dictionaries, write a function that transforms it into a new structure based on a set of rules (e.g., grouping by a specific key).
"""
from collections import defaultdict
def transform_data(data, name):
    res = defaultdict(list)
    for item in data:
        res[item["name"]].append(item["score"])

    return res


data = [{"name": "Alice", "score": 90}, {"name": "Bob", "score": 85}, {"name": "Alice", "score": 95}]
print(transform_data(data, "name"))
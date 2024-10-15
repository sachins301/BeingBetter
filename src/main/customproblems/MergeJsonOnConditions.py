"""
Join JSON Data with SQL-like Conditions: 
Given two lists of dictionaries, write a function that joins them based on specific keys (mimicking SQL joins).
"""

def join_data(data1, data2, condition):
    res = []
    for item1 in data1:
        for item2 in data2:
            if item1[condition] == item2[condition]:
                res.append({**item1, **item2})
    return res


data1 = [{"user_id": 1, "name": "Alice"}]
data2 = [{"user_id": 1, "country": "USA"}]
print(join_data(data1, data2, "user_id"))
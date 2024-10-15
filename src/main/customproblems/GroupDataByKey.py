"""
Group Data by Key
Write a function to group a list of dictionaries by a specific key (like grouping users by country) and return aggregate metrics such as total sales.
"""

from collections import defaultdict


def group_by_key(sales_data, key):
    res = defaultdict(dict)
    for sales in sales_data:
        group_key = sales[key]
        for k, v in sales.items():
            if k == key:
                continue
            res[group_key][k] = res[group_key].get(k, 0) + v

    return res

# Example data
sales_data = [
    {"country": "US", "price": 100, "quantity": 2},
    {"country": "US", "price": 150, "quantity": 1},
    {"country": "UK", "price": 200, "quantity": 3},
    {"country": "UK", "price": 120, "quantity": 1}
]

print(group_by_key(sales_data, "country"))
"""
Extract and Summarize Nested Data: 
Write a function that extracts specific fields from a nested dictionary (e.g., product orders) and summarizes total order value, quantities, etc.
"""

from collections import defaultdict


def extract_and_summarize(orders):
    res = defaultdict(lambda : {"total_order_value" : 0, "quantities" : 0})
    for order in orders:
        for item in order["items"]:
            prod_id = item["product"]
            res[prod_id]["total_order_value"] += item["price"] * item["quantity"]
            res[prod_id]["quantities"] += item["quantity"]

    return res

# Example nested data
orders = [
    {
        "order_id": 1,
        "items": [
            {"product": "A", "price": 50, "quantity": 2},
            {"product": "B", "price": 100, "quantity": 1}
        ]
    },
    {
        "order_id": 2,
        "items": [
            {"product": "C", "price": 150, "quantity": 1},
            {"product": "A", "price": 50, "quantity": 3}
        ]
    }
]

print(extract_and_summarize(orders))
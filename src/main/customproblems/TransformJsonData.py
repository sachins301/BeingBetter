"""
Transform JSON Data: 
Given JSON input representing sales data, write a function that generates summary metrics like total revenue, 
average sales per user, and the best-selling product.
"""

from collections import defaultdict


def generate_summary(sales):
    res = {"total_revenue" : 0, "total_sales": 0, "average_sales" : 0, "best-selling" : "", "item_sales" : {}}
    for order in sales:
        res["total_revenue"] += order["price"]
        res["total_sales"] += 1
        res["average_sales"] = res["total_revenue"] / res["total_sales"]

        if order["item"] in res["item_sales"]:
            res["item_sales"][order["item"]] += 1
        else:
            res["item_sales"][order["item"]] = 1
        if (not res["best-selling"]) or res["item_sales"][order["item"]] > res["item_sales"][res["best-selling"]]:
            res["best-selling"] = order["item"]
    return res




sales = [{"item": "A", "price": 100}, {"item": "B", "price": 150}]
print(generate_summary(sales))
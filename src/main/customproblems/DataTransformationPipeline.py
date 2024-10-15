"""
Data Transformation Pipeline: 
Write a Python function that takes a stream of events (e.g., clicks, purchases) and transforms it into a summary table of aggregated metrics 
(e.g., total purchases by user).
"""

from collections import defaultdict


def process_logs(logs):
    res = defaultdict(lambda : {"total_purchases" : 0, "total_clicks" : 0})
    for log in logs:
        uid = log["user_id"]
        res[uid]["total_purchases"] += log["purchases"]
        res[uid]["total_clicks"] += log["clicks"]
    return res


logs = [{"user_id": 1, "clicks": 5, "purchases": 1}, {"user_id": 1, "clicks": 3, "purchases": 2}]
print(process_logs(logs))
"""
Real-time Data Aggregation: 
Implement a real-time aggregator that processes incoming logs or events and updates user-level metrics (e.g., total watch time, last login) on the fly.
"""

from collections import defaultdict


def aggregate_realtime(logs):
    res = defaultdict(lambda : {"total_watch_time" : 0, "last_login" : ""})
    for log in logs:
        uid = log["user_id"]
        res[uid]["total_watch_time"] += log["watch_time"]
        res[uid]["last_login"] = log["login_time"]
    return res

logs = [{"user_id": 1, "watch_time": 30, "login_time": "2023-10-01"}]
print(aggregate_realtime(logs))
"""
User Engagement Analysis: 
Write a function that processes a log of user activities (in JSON format) and calculates engagement 
metrics like time spent and number of interactions per user.
"""

from collections import defaultdict


def engagement_metrics(logs):
    res = defaultdict(lambda : {"total_time_spent" : 0, "total_interactions" : 0})
    for log in logs:
        uid = log["user_id"]
        res[uid]["total_time_spent"] += log["time_spent"]
        res[uid]["total_interactions"] += log["interactions"]
    return res



logs = [{"user_id": 1, "time_spent": 30, "interactions": 5}]
print(engagement_metrics(logs))
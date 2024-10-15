"""
Streaming Data Aggregator: 
Write a function that takes a stream of user activity logs and calculates total watch time and unique views per user.
"""

from collections import defaultdict


def aggregate_stream(logs):
    result = defaultdict(lambda : {"total_watch_time" : 0, "unique_views" : set()})
    for log in logs:
        uid = log["user_id"]
        result[uid]["total_watch_time"] += log["watch_time"]
        result[uid]["unique_views"].add(log["video_id"])

    return result




logs = [{"user_id": 1, "video_id": 101, "watch_time": 30}, {"user_id": 1, "video_id": 101, "watch_time": 15}]
print(aggregate_stream(logs))
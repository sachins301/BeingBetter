"""
Calculate Metrics from Nested Data: 
Parse a JSON structure containing user data and return a dictionary summarizing key metrics like average engagement, total posts, etc.
"""


def summarize_metrics(data):
    summary = {}
    for user in data:
        uid = user["user_id"]
        if uid not in summary:
            summary[uid] = {"total_posts" : 0, "total_likes" : 0, "avg_likes" : 0}
        summary[uid]["total_posts"] += user["posts"]
        summary[uid]["total_likes"] += user["likes"]
        summary[uid]["avg_likes"] = summary[uid]["total_likes"] / summary[uid]["total_posts"]
    return summary




data = [{"user_id": 1, "posts": 5, "likes": 100}, {"user_id": 1, "posts": 3, "likes": 50}]
print(summarize_metrics(data))
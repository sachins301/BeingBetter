"""
Write a function that parses a list of user activity logs represented as a list of dictionaries and summarizes
metrics such as total number of posts, average number of comments, and total number of likes per user.
"""
from collections import defaultdict

# Test case
activity_logs = [
    {"user_id": 1, "post_id": 101, "comments": 5, "likes": 10},
    {"user_id": 2, "post_id": 102, "comments": 3, "likes": 8},
    {"user_id": 1, "post_id": 103, "comments": 4, "likes": 7},
    {"user_id": 2, "post_id": 104, "comments": 6, "likes": 9},
    {"user_id": 1, "post_id": 105, "comments": 2, "likes": 4},
]
"""
Expected Output:

python
Copy code
{
    1: {"total_posts": 3, "avg_comments": 3.67, "total_likes": 21},
    2: {"total_posts": 2, "avg_comments": 4.5, "total_likes": 17}
}
"""
def summarize_user_metrics(activity_logs):
    summary = defaultdict(lambda: {"total_posts": 0, "avg_comments": 0, "total_likes": 0})
    for log in activity_logs:
        user = log["user_id"]
        post_id = log["post_id"]
        comments = log["comments"]
        likes = log["likes"]
        summary[user]["total_posts"] += 1
        summary[user]["avg_comments"] = ((summary[user]["avg_comments"] * (summary[user]["total_posts"] - 1)) + comments) / summary[user]["total_posts"]
        summary[user]["total_likes"] += likes
    return summary

print(summarize_user_metrics(activity_logs))
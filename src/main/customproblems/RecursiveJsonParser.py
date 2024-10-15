"""
Recursive JSON Parser
Write a function that recursively parses a deeply nested JSON structure and returns a summary of all leaf nodes. 
We'll sum numeric values and count occurrences of non-numeric values.
"""

def recursive_json_parser(data, summary = None):
    if summary is None:
        summary = {"total_sum": 0, "non_numeric_count": 0}
    
    if isinstance(data, dict):
        for key, value in data.items():
            recursive_json_parser(value, summary)
    
    elif isinstance(data, list):
        for item in data:
            recursive_json_parser(item, summary)
    
    elif isinstance(data, (int, float)):
        summary["total_sum"] += data
    
    else:
        summary["non_numeric_count"] += 1
    
    return summary



# Example nested JSON data
nested_data = {
    "order_1": {
        "price": 100,
        "items": [
            {"name": "A", "quantity": 2},
            {"name": "B", "quantity": 1}
        ]
    },
    "order_2": {
        "price": 200,
        "items": [
            {"name": "C", "quantity": 3},
            {"name": "A", "quantity": 1}
        ]
    }
}

print(recursive_json_parser(nested_data))
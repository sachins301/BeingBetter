"""
Write a Python function that constructs a dynamic SQL query from two input JSON structures. 
The first JSON defines the table and columns, and the second JSON defines the filter conditions.
"""

# Test case
table_json = {
    "table": "users",
    "columns": ["id", "name", "email"]
}

filter_json = {
    "conditions": {
        "age": {"operator": ">", "value": 30},
        "country": {"operator": "=", "value": "US"}
    }
}
# Expected : SELECT id, name, email FROM users WHERE age > 30 AND country = 'US';


def construct_sql_query(table_json, filter_json):
    cols = ', '.join(table_json['columns'])
    query = f"select {cols} from {table_json['table']}"
    where = []
    for k, v in filter_json['conditions'].items():
        condition = k + v['operator'] + str(f"'{v['value']}'" if isinstance(v['value'], str) else v['value'])
        where.append(condition)
        print(condition)
    if where:
        query += ' WHERE ' + ' AND '.join(where)
    return query

print(construct_sql_query(table_json, filter_json))
'''
Write a function that flattens a nested dictionary, where nested dictionaries are represented by dot notation in the keys.
'''

def flatten_dict(input_dict, parent_key = ''):
    output_dict = {}
    for k, v in input_dict.items():
        new_key = parent_key + '.' + k if parent_key else k
        if isinstance(v, dict):
            output_dict.update(flatten_dict(v, new_key))
        else:
            output_dict[new_key] = v
    return output_dict
# Test case
input_dict = {
    "user": {
        "id": 1,
        "name": {
            "first": "John",
            "last": "Doe"
        }
    },
    "posts": {
        "post1": {
            "title": "First Post",
            "content": "Hello, world!"
        },
        "post2": {
            "title": "Second Post",
            "content": "More content"
        }
    }
}

print(flatten_dict(input_dict))
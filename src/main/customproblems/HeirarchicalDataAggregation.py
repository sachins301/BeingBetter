"""
Hierarchical Data Aggregation: 
Write a function that processes hierarchical data (e.g., company org charts or nested categories) and returns the total count of items at each level.
"""

from collections import defaultdict


def count_levels(tree):
    levels = defaultdict(int)
    def traverse(node, level):
        levels[level] += 1
        for child in node.get("children", []):
            traverse(child, level + 1)

        return

    traverse(tree, 0)
    return levels


tree = {"name": "root", "children": [{"name": "child1"}, {"name": "child2", "children": [{"name": "child2_1"}]}]}
print(count_levels(tree))
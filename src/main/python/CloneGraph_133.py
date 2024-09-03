# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        copyMap = {}

        def dfs(node):
            if node in copyMap:
                return copyMap[node]
            copy = Node(node.val)
            copyMap[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            return copy

        return dfs(node)

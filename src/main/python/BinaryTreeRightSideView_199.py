# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, currdepth):
            if not node:
                return
            if currdepth == len(res):
                res.append(node.val)
            dfs(node.right, currdepth + 1)
            dfs(node.left, currdepth + 1)

        dfs(root, 0)
        return res
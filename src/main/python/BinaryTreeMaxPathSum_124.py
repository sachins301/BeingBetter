# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')

        def dfs(node):
            if not node:
                return 0
            rightsum = max(dfs(node.right), 0)
            leftsum = max(dfs(node.left), 0)
            self.res = max(self.res, rightsum + leftsum + node.val)
            return max(rightsum, leftsum) + node.val
        dfs(root)
        return self.res
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def rec(node, lref, rref):
            if not node:
                return True
            if not (node.val > lref and node.val < rref):
                return False
            return rec(node.left, lref, node.val) and rec(node.right, node.val, rref)

        return rec(root, float('-inf'), float('inf'))
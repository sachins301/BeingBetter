from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None

        def rec(node):
            if not node:
                return
            rec(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
            rec(node.right)
            return
        rec(root)

        return self.res
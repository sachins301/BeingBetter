# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node, maxv):
            if not node:
                return
            if node.val >= maxv:
                self.res += 1
            dfs(node.right, max(maxv, node.val))
            dfs(node.left, max(maxv, node.val))
        dfs(root, root.val)
        return self.res
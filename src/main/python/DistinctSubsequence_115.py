class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def helper(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = helper(i + 1, j)
            if s[i] == t[j]:
                res += helper(i + 1, j + 1)
            dp[(i, j)] = res
            return res
        return helper(0, 0)
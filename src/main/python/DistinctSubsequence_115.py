class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        # for row in dp:
        #     print(row)
        return dp[0][0]


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
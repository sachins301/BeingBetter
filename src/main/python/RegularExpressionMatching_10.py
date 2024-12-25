from collections import defaultdict


class Solution:


    def isMatch(self, s: str, p: str) -> bool:
        dp = defaultdict(int)

        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[len(s)][len(p)] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                match = (i < len(s) and (s[i] == p[j] or p[j] == '.'))
                if j + 1 < len(p) and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or (match and dp[i + 1][j])
                elif match:
                    dp[i][j] = dp[i + 1][j + 1]
        return dp[0][0]



def isMatch(self, s: str, p: str) -> bool:
        dp = defaultdict(int)

        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False
            if (i, j) in dp:
                return dp[(i, j)]
            print(i, j)
            if j + 1 < len(p) and p[j + 1] == "*":
                dp[(i, j)] = dfs(i, j + 2) or ((i < len(s) and (s[i] == p[j] or p[j] == '.')) and dfs(i + 1, j))
            elif i < len(s) and j < len(p) and (s[i] == p[j] or p[j] == '.'):
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = False
            return dp[(i, j)]

        return dfs(0, 0)
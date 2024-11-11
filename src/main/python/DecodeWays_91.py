class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s) + 1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n):
            one = int(s[i - 1])
            two = int(s[i - 2 : i])
            if one != 0:
                dp[i] += dp[i - 1]
            if two > 9 and two < 27:
                dp[i] += dp[i - 2]
        return dp[n - 1]

    # recursion and memoization
    def numDecodings_rec(self, s: str) -> int:
        res = 0
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(s):
                res = 1
            elif s[i] == '0':
                res = 0
            elif int(s[i : i + 2]) > 9 and  int(s[i : i + 2]) < 27:
                res = dfs(i + 1) + dfs(i + 2)
            else: res = dfs(i + 1)
            dp[i] = res
            return res
        return dfs(0)

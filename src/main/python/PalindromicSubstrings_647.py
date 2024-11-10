class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l = i - 1
            r = i + 1
            res += 1
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                res += 1
                l -= 1
                r += 1

            l = i - 1
            r = i
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                res += 1
                l -= 1
                r += 1
        return res

    #dynamic programming
    def countSubstrings_dp(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for i in range(n)]
        res = 0
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j + 1 <= 2 or dp[i-1][j+1]):
                    res += 1
                    dp[i][j] = True
        return res
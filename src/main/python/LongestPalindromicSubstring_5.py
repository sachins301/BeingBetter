class Solution:

    #Dynamic Programming
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLen = 0
        n = len(s)
        dp = [[False] * n for i in range(n)]

        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and (i - j <= 1 or dp[i-1][j+1] == True):
                    dp[i][j] = True
                    # print('im here', resLen, i , j, s[j : i + 1])
                    if resLen < i - j + 1:
                        resLen = i - j + 1
                        res = s[j : i + 1]
        return res
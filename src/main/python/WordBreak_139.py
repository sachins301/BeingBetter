from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                wlen = len(word)
                if i + wlen <= len(s) and word == s[i : i + wlen]:
                    dp[i] = dp[i + wlen]
                if dp[i]:
                    break
        return dp[0]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def helper(i):
            if i in dp:
                return dp[i]
            for word in wordDict:
                n = len(word)
                if word == s[i:i+n]:
                    if i+n == len(s) or helper(i+n):
                        dp[i] = True
                        return True
            dp[i] = False
            return False
        return helper(0)
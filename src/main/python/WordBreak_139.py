from typing import List


class Solution:
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
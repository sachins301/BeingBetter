from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(rem):
            if rem == 0 :
                return 0
            if rem in dp:
                return dp[rem]
            res = float('inf')
            for c in coins:
                if rem - c >= 0:
                    res = min(res, 1 + dfs(rem - c))
            dp[rem] = res
            return res
        res = dfs(amount)
        return res if res != float('inf') else -1
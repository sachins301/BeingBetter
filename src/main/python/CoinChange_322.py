from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != float('inf') else -1


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
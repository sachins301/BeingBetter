from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices) + 1)]
        for i in range(len(prices) - 1, -1, -1):
            for buying in [True, False]:
                if buying:
                    buy = dp[i + 1][False] - prices[i]
                    cooldown = dp[i + 1][True]
                    dp[i][buying] = max(buy, cooldown)
                else:
                    sell = dp[i + 2][True] + prices[i] if i + 2 < len(prices) + 1 else prices[i]
                    cooldown = dp[i + 1][False]
                    dp[i][buying] = max(sell, cooldown)
        return dp[0][True]

    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def helper(i, holding):
            if i >= len(prices):
                return 0
            if (i, holding) in dp:
                return dp[(i, holding)]
            if holding:
                sell = helper(i + 2, False) + prices[i]
                hold = helper(i + 1, True)
                dp[(i, holding)] = max(sell, hold)
            else:
                buy = helper(i + 1, True) - prices[i]
                hold = helper(i + 1, False)
                dp[(i, holding)] = max(buy, hold)
            return dp[(i, holding)]
        return helper(0, False)
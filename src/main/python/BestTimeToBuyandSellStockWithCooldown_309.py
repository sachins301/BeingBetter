from typing import List


class Solution:
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
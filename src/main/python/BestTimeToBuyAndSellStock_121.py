from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy, sell = 0, 1
        while(sell < len(prices)):
            if prices[buy] < prices[sell]:
                res = max(res, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        return res
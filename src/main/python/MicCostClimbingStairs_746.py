from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        dp = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            dp.append(min(cost[i] + dp[i-1], cost[i] + dp[i-2]))
        return dp[-1]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i + 2])
        return min(cost[0], cost[1])
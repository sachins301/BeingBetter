from typing import List


class Solution:

    # recursion
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def helper(i, t):
            if t == 0:
                return 1
            if i >= len(coins) or t < 0:
                return 0
            if (i, t) in dp:
                return dp[(i, t)]
            dp[(i, t)] =  helper(i + 1, t) + helper(i, t - coins[i])
            return dp[(i, t)]
        return helper(0, amount)

    # dp
    class Solution:
        def change(self, amount: int, coins: List[int]) -> int:
            dp = [0] * (amount + 1)
            dp[0] = 1
            for i in range(len(coins) - 1, -1, -1):
                for j in range(1, 1 + amount):
                    dp[j] += dp[j - coins[i]] if j - coins[i] >= 0 else 0
            return dp[amount]

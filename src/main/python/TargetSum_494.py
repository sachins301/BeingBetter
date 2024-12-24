from collections import defaultdict
from typing import List


class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1

        for i in range(len(nums)):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count
        # print(dp)
        return dp[len(nums)][target]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = [0]
        i = 0
        dp = defaultdict(int)
        def helper(i, t):
            if (i, t) in dp:
                return dp[(i, t)]
            if i == len(nums):
                return 1 if t == 0 else 0

            dp[(i, t)] = helper(i + 1, t - nums[i]) + helper(i + 1, t + nums[i])
            return dp[(i, t)]

        return helper(0, target)
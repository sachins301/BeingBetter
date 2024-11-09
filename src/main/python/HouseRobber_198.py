from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def helper(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            dp[i] = max(helper(i + 2) + nums[i], helper(i + 1))
            return dp[i]
        return helper(0)


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

    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i-2], nums[i-1])
        return nums[-1]

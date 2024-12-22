from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        if len(nums) == 1:
            return nums[0]

        def helper(i, m):
            if i >= m:
                return 0
            if i in dp:
                return dp[i]
            dp[i] = max(helper(i + 2, m) + nums[i], helper(i + 1, m))
            return dp[i]

        res1 = helper(0, len(nums) - 1)
        dp = {}
        res2 = helper(1, len(nums))

        return max(res1, res2)

    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        def helper(nums):
            rob1, rob2 = 0, 0
            for i in range(len(nums)):
                temp = max(rob1 + nums[i], rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(helper(nums[:-1]), helper(nums[1:]))
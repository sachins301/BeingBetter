from typing import List


class Solution:
    # recursion and memoization
    def lengthOfLIS(self, nums: List[int]) -> int:
        n= len(nums)
        dp = [[-1] * (n + 1) for _ in range(n)]

        def helper(curr, prev):
            if curr == len(nums):
                return 0
            if dp[curr][prev + 1] != -1:
                return dp[curr][prev + 1]
            res = helper(curr + 1, prev)
            if prev == -1 or nums[curr] > nums[prev]:
                res = max(res, 1 + helper(curr + 1, curr))
            dp[curr][prev + 1] = res
            return res
        return helper(0 , -1)

    # DP
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)


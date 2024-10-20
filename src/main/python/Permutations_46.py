from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def helper(nums):
            if not nums:
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                subset.append(nums[i])
                helper(nums[:i] + nums[i+1:])
                subset.pop()
            return
        helper(nums)
        return res
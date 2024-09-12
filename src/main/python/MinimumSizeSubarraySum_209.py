from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        res = len(nums)
        l = 0
        s = 0
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                res = min(res, r - l + 1)
                s -= nums[l]
                l += 1

        return res
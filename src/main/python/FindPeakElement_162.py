from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            l = nums[i-1] if i > 0 else float('-inf')
            r = nums[i+1] if i < len(nums) - 1 else float('-inf')
            if nums[i] > l and nums[i] > r:
                return i


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
            else:
                nums[i - cnt] = nums[i]
        for i in range(len(nums) - cnt, len(nums)):
            nums[i] = 0
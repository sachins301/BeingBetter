from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            num = abs(nums[i])
            if num - 1 >= 0 and num - 1 < len(nums):
                if nums[num - 1] == 0:
                    nums[num - 1] = len(nums) * -1
                elif nums[num - 1] > 0:
                    nums[num - 1] *= -1

        # print(nums)

        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1
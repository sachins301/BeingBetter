from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums = set(nums)
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i

        num_s = sum(nums)
        n = len(nums)
        s = n * (n + 1) / 2
        return int(s - num_s)
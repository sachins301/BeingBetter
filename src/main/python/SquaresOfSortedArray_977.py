from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        curr = len(nums) - 1
        l = 0
        r = len(nums) - 1
        l2 = nums[l] ** 2
        r2 = nums[r] ** 2
        res = [0] * len(nums)
        while l <= r:
            if l2 > r2:
                res[curr] = l2
                l += 1
                l2 = nums[l] ** 2
            else:
                res[curr] = r2
                r -= 1
                r2 = nums[r] ** 2
            curr -= 1
        return res

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin, res = 1, 1, max(nums)
        for n in nums:
            currMax, currMin = max(n * currMax, n * currMin, n), min(n * currMax, n * currMin, n)
            res = max(currMax, currMin, res)
        return res
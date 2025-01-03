from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        curr = 0
        for n in nums:
            curr += n
            res = max(res, curr)
            if curr < 0:
                curr = 0

        return res
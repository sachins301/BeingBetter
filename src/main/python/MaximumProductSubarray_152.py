from typing import List

# Kadane's Algorithm
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin, res = 1, 1, max(nums)
        for n in nums:
            currMax, currMin = max(n * currMax, n * currMin, n), min(n * currMax, n * currMin, n)
            res = max(currMax, currMin, res)
        return res

    def maxProduct(self, nums: List[int]) -> int:
        pre = 1
        res = nums[0]
        for n in nums:
            if pre == 0:
                pre = 1
            pre *= n
            res = max(res, pre)
        post = 1
        for n in nums[::-1]:
            if post == 0:
                post = 1
            post *= n
            res = max(res, post)
        return res
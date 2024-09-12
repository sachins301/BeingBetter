from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        res = []
        for num in nums1:
            if num in next_greater:
                res.append(next_greater[num])
            else:
                res.append(-1)
        return res

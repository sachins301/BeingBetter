from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        for n in nums1:
            if n in nums2:
                res.add(n)
        return list(res)
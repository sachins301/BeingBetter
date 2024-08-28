from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        lmax = height[l]
        rmax = height[r]
        while l < r:
            if lmax < rmax:
                res += lmax - height[l]
                l += 1
                lmax = max(height[l], lmax)
            else:
                res += rmax - height[r]
                r -= 1
                rmax = max(height[r], rmax)
        return res
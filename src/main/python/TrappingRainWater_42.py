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

    # post and pre fill
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        lmax = [0] * n
        rmax = [0] * n

        lmax[0] = height[0]
        for i in range(1, n):
            lmax[i] = max(lmax[i-1], height[i])
        rmax[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            rmax[i] = max(rmax[i + 1], height[i])
        res = 0
        for i in range(n):
            res += min(lmax[i], rmax[i]) - height[i]
        return res
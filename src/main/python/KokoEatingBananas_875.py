from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while(l <= r):
            mid = (l + r) // 2
            hrs = 0
            for p in piles:
                hrs += (p + (mid - 1))//mid
            if hrs > h:
                l = mid + 1
            else:
                res = min(res, mid)
                r = mid - 1
        return res

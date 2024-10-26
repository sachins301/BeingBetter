from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        for i in arr:
            res.append((abs(x - i), i))
        res.sort()
        return sorted([i for d, i in res[:k]])
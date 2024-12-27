from collections import defaultdict
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seat = defaultdict(set)
        for r, c in reservedSeats:
            if c == 1 or c == 10:
                continue
            if c in {4, 5}:
                seat[r].add(0)
                seat[r].add(1)
            elif c in {6,7}:
                seat[r].add(1)
                seat[r].add(2)
            elif c in {2, 3}:
                seat[r].add(0)
            elif c in {8, 9}:
                seat[r].add(2)
        res = n * 2
        for r in seat:
            if len(seat[r]) == 3:
                res -= 2
            else:
                res -= 1
        return res



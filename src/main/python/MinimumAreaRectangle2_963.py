from math import sqrt
from collections import defaultdict
from typing import List


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        centers = defaultdict(list)
        res = float('inf')
        for i, (x,y) in enumerate(points):
            for x1, y1 in points[i+1:]:
                cx = (x + x1) / 2
                cy = (y + y1) / 2
                d = (x - x1)**2 + (y - y1)**2

                for p in centers[(cx, cy, d)]:
                    area = sqrt(((x - p[0])**2 + (y - p[1])**2) * ((x1 - p[0])**2 + (y1 - p[1])**2))
                    res = min(res, area)

                centers[(cx, cy, d)].append((x, y))

        return res if res < float('inf') else 0
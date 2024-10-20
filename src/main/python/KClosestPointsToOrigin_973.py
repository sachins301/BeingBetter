import heapq

import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x1, y1 in points:
            dist = math.sqrt((x1)**2 + y1**2)
            minheap.append((dist, [x1, y1]))
        heapq.heapify(minheap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res
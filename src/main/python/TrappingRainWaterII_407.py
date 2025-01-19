import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        minheap = []
        visit = set()
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROW, COL = len(heightMap), len(heightMap[0])
        for i in range(ROW):
            for j in range(COL):
                if i == 0 or i == ROW - 1 or j == 0 or j == COL - 1:
                    heapq.heappush(minheap, (heightMap[i][j], i, j))
                    visit.add((i, j))
        res = 0
        maxheight = -1
        while minheap:
            h, r, c = heapq.heappop(minheap)
            maxheight = max(maxheight, h)
            res += maxheight - h
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 < nr < ROW - 1 and 0 < nc < COL - 1 and (nr, nc) not in visit:
                    heapq.heappush(minheap, (heightMap[nr][nc], nr, nc))
                    visit.add((nr, nc))
        return res

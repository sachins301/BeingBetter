import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set((0,0))
        minheap = [(grid[0][0], 0, 0)] #starting position
        heapq.heapify(minheap)
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while minheap:
            currmax, curri, currj = heapq.heappop(minheap)
            if curri == len(grid)-1 and currj == len(grid[0])-1:
                return currmax
            for i, j in dirs:
                ni, nj = i + curri, j + currj
                if (ni, nj) not in visited and ni < len(grid) and nj < len(grid[0]) and ni >= 0 and nj >= 0:
                    visited.add((ni, nj))
                    heapq.heappush(minheap, (max(currmax, grid[ni][nj]), ni, nj))
        return
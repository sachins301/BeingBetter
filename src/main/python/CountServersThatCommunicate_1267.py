from collections import defaultdict
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = defaultdict(int)
        col = defaultdict(int)
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    row[r] += 1
                    col[c] += 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (row[r] > 1 or col[c] > 1):
                    res += 1
        return res
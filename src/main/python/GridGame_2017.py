from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        top, bottom = sum(grid[0][1:]), 0
        res = top
        for i in range(1, len(grid[0])):
            top -= grid[0][i]
            bottom += grid[1][i - 1]
            res = min(res, max(top, bottom))
        return res
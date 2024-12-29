from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()
        dirs = [[1, 0],[0, 1], [-1, 0], [0, -1]]
        dp = {}
        def dfs(r, c):
            res = 0
            # if (r, c) in dp:
            #     return dp[(r, c)]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < COL and (nr, nc) not in visit and grid[nr][nc] != 0:
                    visit.add((nr, nc))
                    res = max(res, dfs(nr, nc))
                    visit.remove((nr, nc))
            # dp[(r, c)] = res + grid[r][c]
            return res + grid[r][c]
        res = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] != 0:
                    visit.add((i, j))
                    res = max(res, dfs(i, j))
                    visit.remove((i, j))
        return res

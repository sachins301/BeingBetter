from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited = set()
        res = [0]
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(r, c):
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if nr < row and nc < col and nr >= 0 and nc >= 0 and grid[nr][nc] == 1:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        dfs(nr, nc)
                else:
                    res[0] += 1

        for r in range(row):
            for c in range(col):
                if (r, c) not in visited and grid[r][c] == 1:
                    visited.add((r, c))
                    dfs(r, c)
        return res[0]
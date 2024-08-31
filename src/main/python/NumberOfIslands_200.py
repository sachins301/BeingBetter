from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        island = 0

        def bfs(row, col):
            stack = []
            stack.append((row, col))
            # visited.add(row, col)
            while stack:
                r, c = stack.pop()
                direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for x, y in direction:
                    nr, nc = r + y, c + x
                    if (nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0])
                            and (nr, nc) not in visited and grid[nr][nc] == "1"):
                        stack.append((nr, nc))
                        visited.add((nr, nc))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    visited.add((i, j))
                    bfs(i, j)
                    island += 1
        return island
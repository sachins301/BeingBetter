import collections
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0

        def bfs(row, col):
            area = 1
            queue = collections.deque()
            queue.append((row, col))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while queue:
                r, c = queue.popleft()
                for direction in directions:
                    nr, nc = r + direction[0], c + direction[1]
                    if ((nr, nc) not in visited and nr >= 0 and nr < len(grid) and
                            nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 1):
                        queue.append((nr, nc))
                        visited.add((nr,nc))
                        area += 1
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == 1:
                    visited.add((i,j))
                    area = bfs(i, j)
                    maxArea = max(maxArea, area)

        return maxArea
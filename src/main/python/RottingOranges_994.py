from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        stack = deque()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    stack.append([i, j])
                if grid[i][j] == 1:
                    fresh += 1

        while stack and fresh > 0:
            for i in range(len(stack)):
                r, c = stack.popleft()
                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]
                    if (nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and
                            grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        stack.append([nr, nc])
                        fresh -= 1
            minutes += 1

        return minutes if fresh == 0 else -1


    def orangesRotting_stack(self, grid: List[List[int]]) -> int:
        self.minutes = 0
        stack = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        def graph_traversal():
            while stack:
                new_rotten_batch = []

                for r, c in stack.pop():
                    for d in directions:
                        nr = r + d[0]
                        nc = c + d[1]
                        if (nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and
                                (nr, nc) not in visited and grid[nr][nc] == 1):
                            grid[nr][nc] = 2
                            visited.add((nr, nc))
                            new_rotten_batch.append([nr, nc])
                # print(new_rotten_batch)
                if new_rotten_batch:
                    self.minutes += 1
                    stack.append(new_rotten_batch)

        day0 = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2 and (i, j) not in visited:
                    visited.add((i, j))
                    day0.append([i, j])
        stack.append(day0)
        graph_traversal()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1


        return self.minutes

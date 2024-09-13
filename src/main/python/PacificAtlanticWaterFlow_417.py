from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(r, c, visit, prevHeight):
            if (r, c) in visit or r < 0 or r >= ROWS or c < 0 or c >= COLS or heights[r][c] < prevHeight:
                return
            visit.add((r, c))
            for d in directions:
                dfs(r + d[0], c + d[1], visit, heights[r][c])
            return


        for i in range(ROWS):
            dfs(i, 0, pac, 0)
            dfs(i, COLS - 1, atl, 0)

        for j in range(COLS):
            dfs(0, j, pac, 0)
            dfs(ROWS - 1, j, atl, 0)

        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pac and (i, j) in atl:
                    # do something
                    res.append([i, j])
        return res
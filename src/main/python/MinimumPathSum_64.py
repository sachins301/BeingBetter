from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])
        newgrid = [[float('inf')]*COL for i in range(ROW)]
        newgrid[0][0] = grid[0][0]
        directions = [[0, 1], [1, 0]]
        for i in range(ROW):
            for j in range(COL):
                for d in directions:
                    nr, nc = d[0] + i, d[1] + j
                    if nr >= 0 and nr < ROW and nc >= 0 and nc < COL:
                        # print(i, j, "-->", nr, nc, "-->", newgrid[i][j] + grid[nr][nc], newgrid[nr][nc])
                        newgrid[nr][nc] = min(newgrid[i][j] + grid[nr][nc], newgrid[nr][nc])
                        # print(newgrid)
        return newgrid[ROW - 1][COL - 1]


'''
1   3   1       1   4   5           1   4   5   
1   5   1       2  9>7   6          2   7   6
4   2   1       6   8   7           6   9   7
'''
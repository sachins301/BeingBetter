from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        dp = [[0] * COL for _ in range(ROW)]
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy
                if (nr < ROW and nr >= 0 and nc < COL and nc >= 0 and matrix[nr][nc] > matrix[r][c]):
                    if dp[nr][nc] == 0:
                        dfs(nr, nc)
                    dp[r][c] = max(dp[r][c], dp[nr][nc] + 1)
                else:
                    dp[r][c] = max(dp[r][c], 1)
            return
        res = 0
        for i in range(ROW):
            for j in range(COL):
                if dp[i][j] == 0:
                    dfs(i, j)
                res = max(res, dp[i][j])
        return res
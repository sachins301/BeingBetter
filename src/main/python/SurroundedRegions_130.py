from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def capture(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            for d in directions:
                capture(r+d[0], c+d[1])
            return

        for i in range(ROWS):
            for j in range(COLS):
                if ((i == 0 or i == ROWS - 1 or j == 0 or j == COLS - 1) and board[i][j] == 'O'):
                    capture(i, j)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'T':
                    board[i][j] = 'O'

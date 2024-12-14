from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for i in range(n)]
        col = set()
        pos = set()
        neg = set()

        def helper(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or r + c in pos or r - c in neg:
                    continue
                board[r][c] = 'Q'
                col.add(c)
                pos.add(r + c)
                neg.add(r - c)
                helper(r + 1)
                board[r][c] = '.'
                col.remove(c)
                pos.remove(r + c)
                neg.remove(r - c)
            return
        helper(0)
        return res
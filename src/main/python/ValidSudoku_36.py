from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = set() #(rowId, Number)
        colSet = set() #(colId, Number)
        gridSet = set() #(rowId // 3, colId // 3, Number)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if ((i, board[i][j]) in rowSet or
                        (j, board[i][j]) in colSet or (i // 3, j // 3, board[i][j]) in gridSet):
                    return False
                rowSet.add((i, board[i][j]))
                colSet.add((j, board[i][j]))
                gridSet.add((i // 3, j // 3, board[i][j]))

        return True
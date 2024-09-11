from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r, c, pos, visited):
            if pos == len(word):
                return True
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if (nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0])
                        and board[nr][nc] == word[pos] and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    if dfs(nr, nc, pos+1, visited):
                        return True
                    visited.remove((nr, nc))
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if dfs(i, j, 1, visited):
                        return True

        return False

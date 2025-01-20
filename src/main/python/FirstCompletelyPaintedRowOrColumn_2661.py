from collections import defaultdict
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        paintedrow = defaultdict(int)
        paintedcol = defaultdict(int)
        m, n = len(mat), len(mat[0])
        position = {}
        for i in range(m):
            for j in range(n):
                position[mat[i][j]] = (i, j)
        for i in range(len(arr)):
            r, c = position[arr[i]]
            paintedrow[r] += 1
            paintedcol[c] += 1
            if paintedrow[r] == n or paintedcol[c] == m:
                return i
        return -1
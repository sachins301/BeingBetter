from builtins import int, bool, len
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        col = -1
        l = 0
        r = len(matrix) - 1
        while(l <= r):
            mid = (l + r) // 2
            if matrix[mid][-1] < target:
                l = mid + 1
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                break

        if l > r:
            return False
        row = (l + r) // 2

        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False

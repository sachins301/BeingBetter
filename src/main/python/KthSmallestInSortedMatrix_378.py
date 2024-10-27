import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        combined = []
        for i in range(len(matrix)):
            combined += matrix[i]
        heapq.heapify(combined)
        return heapq.nsmallest(k, combined)[-1]
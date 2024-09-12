from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # for i in range(1, len(arr)):
        #     if arr[i] < arr[i-1]:
        #         return i-1

        l = 0
        r = len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < arr[mid + 1]:
                l = mid + 1
            elif arr[mid] > arr[mid + 1]:
                r = mid
        return l
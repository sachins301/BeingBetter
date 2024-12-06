from bisect import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binarySearch(l, r) -> int:
            if l > r:
                return -1
            mid = (r + l)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return binarySearch(mid+1, r)
            else:
                return binarySearch(l, mid-1)

        return binarySearch(0, len(nums)-1)


    def search_bisect(self, nums: List[int], target: int) -> int:
        mid = bisect.bisect_left(nums, target)
        return mid if mid < len(nums) and nums[mid] == target else -1

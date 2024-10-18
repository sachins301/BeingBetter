from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binarySearch(searchLeft: bool):
            l = 0
            r = len(nums) - 1
            res = -1
            while l <= r:
                mid = (l + r)//2
                if nums[mid] == target:
                    res = mid
                    if searchLeft:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return res

        return [binarySearch(True), binarySearch(False)]
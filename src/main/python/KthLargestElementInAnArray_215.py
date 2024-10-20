import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # # Quick Select
        # # index of kth largest element in a sorted list
        # k = len(nums) - k
        # def quickSelect(l, r):
        #     # consider r as pivot
        #     pivot = nums[r]
        #     curr_pos = l
        #     for i in range(l, r):
        #         if nums[i] <= pivot:
        #             nums[curr_pos], nums[i] = nums[i], nums[curr_pos]
        #             curr_pos += 1
        #     nums[curr_pos], nums[r] = nums[r], nums[curr_pos]

        #     if curr_pos > k : return quickSelect(l, curr_pos - 1)
        #     elif curr_pos < k : return quickSelect(curr_pos + 1, r)
        #     else: return nums[curr_pos]

        # return quickSelect(0, len(nums)-1)

        # # SORT SOLUTION
        # nums.sort(reverse = True)
        # return nums[k-1]

        # # HEAP SOLUTION
        heapq.heapify(nums)
        while(len(nums) > k):
            heapq.heappop(nums)
        return heapq.heappop(nums)

        # TIME LIMIT
        # start = 0
        # end = len(nums) - 1
        # for i in range(len(nums)):
        #     start = 0
        #     while(start < end):
        #         if nums[start] > nums[start + 1]:
        #             nums[start], nums[start + 1] = nums[start + 1], nums[start]
        #         start += 1
        #     if end == len(nums) - k:
        #         return nums[end]
        #     end -= 1
        # return nums[end]


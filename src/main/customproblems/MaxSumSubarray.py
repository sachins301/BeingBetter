"""
Sliding Window / Moving Average
Problem: Given an array of integers, find the maximum sum of any contiguous subarray of length k.


Solution: Use the sliding window technique by first summing the first k elements, then sliding the window one element
at a time while adjusting the sum by subtracting the element that goes out of the window and adding the element that
comes into the window."""

def maxSumSubarray(nums, k):
    if len(nums) < k:
        return 0

    # Calculate initial window sum
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage:
nums = [2, 1, 5, 1, 3, 2]
k = 3
print(maxSumSubarray(nums, k))  # Output: 9

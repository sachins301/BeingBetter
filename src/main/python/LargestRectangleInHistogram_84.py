from typing import List


class LargestRectangleInHistogram_84:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #[index, height]
        max_area = 0
        for i in range(len(heights)):
            prev = i
            while stack and stack[-1][1] > heights[i]:
                idx, h = stack.pop()
                max_area = max(max_area, h * (i - idx))
                prev = idx
            stack.append([prev, heights[i]])
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
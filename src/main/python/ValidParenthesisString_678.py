class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = 0
        left_max = 0
        for c in s:
            if c == '(':
                left_min += 1
                left_max += 1
            if c == '*':
                left_min -= 1
                left_max += 1
            if c == ')':
                left_min -= 1
                left_max -= 1
            if left_min < 0:
                left_min = 0
            if left_max < 0:
                return False
        return 0 >= left_min and 0 <= left_max
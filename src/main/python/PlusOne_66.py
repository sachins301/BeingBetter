from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += rem
            if digits[i] > 9:
                rem = digits[i] // 10
                digits[i] %= 10
            else:
                rem = 0
        if rem > 0:
            digits = [rem] + digits
        return digits

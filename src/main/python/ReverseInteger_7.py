class Solution:
    def reverse(self, x: int) -> int:
        if x < -2**31 or x > 2**31 - 1:
            return 0
        sign = 1
        if x < 0:
            sign = -1
            x = -1 * x
        x = sign * int(str(x)[::-1])
        if x < -2**31 or x > 2**31 - 1:
            return 0
        return x
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        sign = -1 if (dividend < 0 and divisor >= 0) or (dividend >= 0 and divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0

        while dividend >= divisor:
            curr_divisor = divisor
            count = 1
            while dividend >= curr_divisor:
                dividend = dividend - curr_divisor
                res += count
                curr_divisor = curr_divisor << 1
                count = count << 1


        return min(2147483647, max(-2147483648, sign * res))
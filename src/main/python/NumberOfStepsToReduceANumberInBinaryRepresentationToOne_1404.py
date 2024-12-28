class Solution:
    def numSteps(self, s: str) -> int:
        res = 0
        carry = 0
        for i in range(len(s) - 1, 0, -1):
            digit = (carry + int(s[i])) % 2
            if digit:
                carry = 1
                res += 2
            else:
                res += 1
        return res + carry

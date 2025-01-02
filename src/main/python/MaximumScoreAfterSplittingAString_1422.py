class Solution:
    def maxScore(self, s: str) -> int:
        zeroes = 0
        ones = 0
        pre = []
        for c in s[:-1]:
            if c == '0':
                zeroes += 1
            pre.append(zeroes)
        pre.append(zeroes)
        res = 0
        for i in range(len(s) - 1, 0, -1):
            if s[i] == '1':
                ones += 1
            res = max(res, ones + pre[i])
        return res

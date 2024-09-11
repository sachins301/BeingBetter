class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        rem = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or rem:
            if i >= 0:
                rem += int(a[i])
                i -= 1
            if j >= 0:
                rem += int(b[j])
                j -= 1
            res = str(rem % 2) + res
            rem = rem // 2
        return res
from collections import Counter


class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        res = ''
        mid = ''
        for d in sorted(count.keys(), reverse = True):
            if count[d] % 2 == 1:
                mid = max(mid, d)
            res += d * (count[d] // 2)
        res = res.lstrip('0')
        res = res + mid + res[::-1]
        return res if res else '0'
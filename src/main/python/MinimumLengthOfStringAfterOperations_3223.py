from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        dic = Counter(s)
        res = len(s)

        for k, v in dic.items():
            while v > 2:
                v -= 2
                res -= 2
        return res
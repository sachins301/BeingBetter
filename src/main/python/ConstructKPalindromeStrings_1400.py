from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        count = Counter(s)
        odd = 0
        for key, v in count.items():
            if v % 2 == 1:
                odd += 1
            if odd > k:
                return False
        return True
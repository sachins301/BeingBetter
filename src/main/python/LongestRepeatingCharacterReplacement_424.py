from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

    # Optimized
    def characterReplacement(self, s: str, k: int) -> int:
        visit = defaultdict(int)
        l = 0
        r = 0
        res = 0
        maxf = 0
        for r in range(len(s)):
            visit[s[r]] += 1
            maxf = max(maxf, visit[s[r]])
            while (r - l + 1) - maxf > k:
                visit[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res


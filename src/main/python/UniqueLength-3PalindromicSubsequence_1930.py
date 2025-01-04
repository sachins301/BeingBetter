from collections import defaultdict, Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = defaultdict(int)
        res = set()
        right = Counter(s)
        for mid in s:
            right[mid] -= 1
            for c in left.keys():
                if right[c] > 0:
                    # print(right.keys(), left, mid, c)
                    res.add(c+mid+c)
            left[mid] += 1

        return len(res)
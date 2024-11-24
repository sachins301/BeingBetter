from collections import defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastChar = defaultdict(int)
        for i in range(len(s)):
            if lastChar[s[i]] < i:
                lastChar[s[i]] = i
        end = 0
        size = 0
        res = []
        for i, c in enumerate(s):
            if lastChar[c] > end:
                end = lastChar[c]
            size += 1
            if i == end:
                res.append(size)
                size = 0
        return res
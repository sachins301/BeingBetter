from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        cnt = []
        tmp = 0
        for w in words:
            if w[0] in {'a', 'e', 'i', 'o', 'u'} and w[-1] in {'a', 'e', 'i', 'o', 'u'}:
                tmp += 1
            cnt.append(tmp)
        res = []
        for i, j in queries:
            tmp = cnt[j]
            if i > 0:
                tmp -= cnt[i - 1]
            res.append(tmp)
        return res
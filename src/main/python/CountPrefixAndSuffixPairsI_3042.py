from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                l = len(words[i])
                if words[i] == words[j][:l] and words[i] == words[j][-l:]:
                    res += 1
        return res
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        b = [0] * 26
        for word in words2:
            temp = [0]*26
            for c in word:
                temp[ord(c) - ord('a')] += 1
            for i in range(26):
                b[i] = max(b[i], temp[i])
        res = []
        # print(b)
        for word in words1:
            a = [0] * 26
            for c in word:
                a[ord(c) - ord('a')] += 1
            flag = True
            # print(a)
            for i in range(26):
                if b[i] > 0 and a[i] < b[i]:
                    flag = False
                    break
            if flag:
                res.append(word)
        return res

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            code = [0] * 26
            for c in s:
                code[ord(c) - ord('a')] += 1
            dic[''.join(str(code))].append(s)
        return list(dic.values())

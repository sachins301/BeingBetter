from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = defaultdict(int)
        for word in words:
            dic[word] += 1
        dic = [(v, k) for k, v in dic.items()]
        dic.sort(key = lambda x: (-x[0], x[1]))
        return [dic[i][1] for i in range(k)]
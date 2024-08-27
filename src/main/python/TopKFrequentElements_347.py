from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        freq = cnt.most_common()
        res = []
        for i in range(k):
            res.append(freq[i][0])
        return res
from collections import Counter, defaultdict
from typing import List

import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        freq = cnt.most_common()
        res = []
        for i in range(k):
            res.append(freq[i][0])
        return res

    #bucket sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            count[n] += 1
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                k -= 1
                if k == 0:
                    return res
        return

    # minheap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        minheap = []
        for key, val in count.items():
            heapq.heappush(minheap, [val, key])
            if len(minheap) > k:
                heapq.heappop(minheap)
        res = []
        while minheap:
            res.append(heapq.heappop(minheap)[1])
        return res
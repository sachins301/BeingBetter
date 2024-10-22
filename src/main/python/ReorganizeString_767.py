import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        prev = ''
        res = ''
        count = Counter(s)
        maxheap = [(-v, k) for k,v in count.items()]
        heapq.heapify(maxheap)
        while maxheap or prev:
            if not maxheap and prev:
                return ""
            count, char = heapq.heappop(maxheap)
            res += char
            count += 1
            if prev:
                heapq.heappush(maxheap, prev)
                prev = None
            if count != 0:
                prev = (count, char)
        return res
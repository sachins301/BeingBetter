import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxheap = [-cnt for cnt in counter.values()]
        heapq.heapify(maxheap)
        q = deque()
        time = 0
        while maxheap or q:
            time += 1
            if maxheap:
                curr = heapq.heappop(maxheap)
                curr += 1
                if curr:
                    q.append((curr, time + n))
            if q and q[0][1] <= time:
                heapq.heappush(maxheap, q.popleft()[0])

        return time

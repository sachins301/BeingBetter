import heapq
from typing import List


class Solution:

    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[0])
        minheap = []
        curr = events[0][0]
        i, n = 0, len(events)
        count = 0
        while(i < n or minheap):
            while i < n and events[i][0] <= curr:
                heapq.heappush(minheap, events[i][1])
                i += 1
            while minheap and minheap[0] < curr:
                heapq.heappop(minheap)
            if(minheap):
                heapq.heappop(minheap)
                count += 1
            curr += 1
        return count

    def maxEvents_timeout(self, events: List[List[int]]) -> int:
        visited = set()
        events.sort(key = lambda x: x[1])
        for s, e in events:
            for curr in range(s, e + 1):
                if curr not in visited:
                    visited.add(curr)
                    break
        return len(visited)

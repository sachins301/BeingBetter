import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        minheap = []
        for cnt, c in [[-a, "a"], [-b, "b"], [-c, "c"]]:
            if cnt:
                heapq.heappush(minheap, [cnt, c])
        res = ""
        while minheap:
            cnt, c = heapq.heappop(minheap)
            if len(res) >= 2 and res[-1] == res[-2] == c:
                if not minheap:
                    break
                cnt2, c2 = heapq.heappop(minheap)
                cnt2 += 1
                res += c2
                if cnt2:
                    heapq.heappush(minheap, [cnt2, c2])
            else:
                cnt += 1
                res += c
            if cnt:
                heapq.heappush(minheap, [cnt, c])
        return res

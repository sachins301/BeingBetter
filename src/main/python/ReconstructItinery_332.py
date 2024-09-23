from typing import List


class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src : [] for src, _ in tickets}
        for src, dst in tickets:
            adj[src].append(dst)
        for src in adj.keys():
            adj[src].sort(reverse=True)
        stack = ['JFK']
        res = []
        while(stack):
            src = stack[-1]
            if src in adj and adj[src]:
                stack.append(adj[src].pop())
            else:
                res.append(stack.pop())
        return res[::-1]

    def findItinerary_timeout(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = {src : [] for src, _ in tickets}
        for src, dst in tickets:
            adj[src].append(dst)
        res = ['JFK']

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            temp = list(adj[src])
            for i, v in enumerate(temp):
                res.append(v)
                adj[src].pop(i)
                if dfs(v): return True
                res.pop()
                adj[src].insert(i, v)
            return False
        dfs('JFK')
        return res
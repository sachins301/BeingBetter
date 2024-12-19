from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True
        visit = set()
        adj = [[] for i in range(n)]
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)
        def dfs(curr, par):
            if curr in visit:
                return False
            visit.add(curr)
            for nei in adj[curr]:
                if nei == par:
                    continue
                if not dfs(nei, curr):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n




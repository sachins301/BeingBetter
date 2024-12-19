from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n
        adj = [[] for i in range(n)]
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        visit = set()
        res = 0
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)
            return
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        return res
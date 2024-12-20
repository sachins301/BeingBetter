from typing import List


class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for i in range(n+1)]
        for s,d in edges:
            adj[s].append(d)
            adj[d].append(s)
        visit = set()
        cycle = set()
        res = []
        cyclestart = [-1]
        def dfs(node, parent):
            if node in visit:
                cyclestart[0] = node
                cycle.add(node)
                return True
            visit.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    if cyclestart[0] != -1:
                        cycle.add(node)
                        if node == cyclestart[0]:
                            cyclestart[0] = -1
                    return True
            return False

        dfs(1, -1)

        for s, d in edges[::-1]:
            if s in cycle and d in cycle:
                return [s, d]




    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += 1
            else:
                parent[p1] = p2
                rank[p2] += 1
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


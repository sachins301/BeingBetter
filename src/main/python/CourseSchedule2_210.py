from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        visitSet = set()
        for crs, preReq in prerequisites:
            preMap[crs].append(preReq)
        res = []

        def dfs(crs):
            if crs in visitSet:
                return False

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            preMap[crs] = []
            visitSet.remove(crs)
            if not crs in res:
                res.append(crs)
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        finish = 0
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        order = []
        while q:
            node = q.popleft()
            finish += 1
            order.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return order[::-1] if finish == numCourses else []
from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = [0] * numCourses
        prereqlist = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            prereq[dst] += 1
            prereqlist[src].append(dst)
        q = deque()
        for i in range(numCourses):
            if prereq[i] == 0:
                q.append(i)
        finish = 0
        while q:
            crs = q.popleft()
            finish += 1
            for nei in prereqlist[crs]:
                prereq[nei] -= 1
                if prereq[nei] == 0:
                    q.append(nei)
        return finish == numCourses

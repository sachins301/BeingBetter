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
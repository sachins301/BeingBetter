from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        goal = set()
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i in range(3):
                if target[i] == t[i]:
                    goal.add(i)

        return True if len(goal) == 3 else False

    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if target in triplets:
            return True
        candidates = [0, 0, 0]
        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            if x == target[0] or y == target[1] or z == target[2]:
                candidates[0] = max(candidates[0], x)
                candidates[1] = max(candidates[1], y)
                candidates[2] = max(candidates[2], z)
        return candidates == target
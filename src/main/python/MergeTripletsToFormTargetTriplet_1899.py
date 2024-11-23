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
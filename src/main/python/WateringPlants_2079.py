from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        can = capacity
        for i in range(len(plants)):
            if plants[i] > can:
                steps += i * 2
                can = capacity
            steps += 1
            can -= plants[i]
        return steps
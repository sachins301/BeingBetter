from typing import List

class CarFleet_853:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for p,s in sorted(zip(position, speed))[::-1]:
            time = (target - p) / s
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)
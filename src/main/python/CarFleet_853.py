from typing import List

class CarFleet_853:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for p,s in sorted(zip(position, speed))[::-1]:
            time = (target - p) / s
            if not stack or stack[-1] < time:
                stack.append(time)

        return len(stack)

    def carFleet_2(self, target: int, position: List[int], speed: List[int]) -> int:
        # 10-1, 8-1, 0-12, 5-7, 3-3
        # 0-12, 3-3, 5-7, 8-1, 10-1

        pairs = [[position[i], (target - position[i])/speed[i]] for i in range(len(position))]
        pairs.sort()
        stack = []
        for p in pairs:
            while stack and p[1] >= stack[-1][1]:
                stack.pop()
            stack.append(p)
            # print(stack)
        return len(stack)
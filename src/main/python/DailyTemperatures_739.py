class DailyTemperatures_739:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [temp, index]
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                idx = stack[-1][1]
                res[idx] = i - idx
                stack.pop()

            stack.append([temperatures[i], i])
        return res
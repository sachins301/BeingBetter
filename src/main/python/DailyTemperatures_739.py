from typing import List


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

    def dailyTemperatures_dp(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]
            if j < n:
                res[i] = j - i
        return res
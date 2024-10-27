class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' in [num1, num2]:
            return '0'
        res = [0]* (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i, n1 in enumerate(num1):
            for j, n2 in enumerate(num2):
                res[i + j] += int(n1) * int(n2)
                res[i + j + 1] += (res[i + j] // 10)
                res[i + j] = res[i + j] % 10
        start = 0
        res = res[::-1]
        while not res[start]:
            start += 1
        res = res[start:]
        res = [str(i) for i in res]
        return ''.join(res)
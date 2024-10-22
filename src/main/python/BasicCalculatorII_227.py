class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        pre = '+'
        stack = []
        s += '+'
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == ' ':
                continue
            else:
                if pre == '+':
                    stack.append(num)
                if pre == '-':
                    stack.append(-num)
                if pre == '*':
                    stack.append(stack.pop() * num)
                if pre == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                pre = c
        return int(sum(stack))
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if stack and c == '+':
                n1 = int(stack.pop())
                stack.append(int(stack.pop()) + n1)
            elif stack and c == '-':
                n1 = int(stack.pop())
                stack.append(int(stack.pop()) - n1)
            elif stack and c == '*':
                n1 = int(stack.pop())
                stack.append(int(stack.pop()) * n1)
            elif stack and c == '/':
                n1 = int(stack.pop())
                stack.append(int(stack.pop()) / n1)
            else:
                stack.append(c)
        return int(stack[0])
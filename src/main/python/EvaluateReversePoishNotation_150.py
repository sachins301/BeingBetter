from typing import List


class EvaluateReversePolishNotation_150:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        for i in tokens:
            if i in ops:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                res = 0
                match i:
                    case '+':
                        res = n1 + n2
                    case '-':
                        res = n1 - n2
                    case '*':
                        res = n1 * n2
                    case '/':
                        res = n1 / n2
                stack.append(int(res))
            else:
                stack.append(int(i))
        print(stack)
        return stack[-1]

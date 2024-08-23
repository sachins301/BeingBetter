from typing import List


class GenerateParantheses_22:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def rec(open_cnt, close_cnt):
            if open_cnt == n and close_cnt == n:
                res.append("".join(stack))
                return
            if open_cnt < n:
                stack.append("(")
                rec(open_cnt + 1, close_cnt)
                stack.pop()
            if close_cnt < open_cnt:
                stack.append(")")
                rec(open_cnt, close_cnt + 1)
                stack.pop()
        rec(0, 0)
        return res
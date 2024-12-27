class Solution:

    def checkValidString(self, s: str) -> bool:
        dp = {}
        def dfs(i, open):
            if open < 0:
                return False
            if i == len(s):
                return True if open == 0 else False
            if (i, open) in dp:
                return dp[(i, open)]
            if s[i] == "(":
                dp[(i, open)] = dfs(i + 1, open + 1)
            elif s[i] == ")":
                dp[(i, open)] = dfs(i + 1, open - 1)
            else:
                dp[(i, open)] = dfs(i + 1, open) or dfs(i + 1, open + 1) or dfs(i + 1, open - 1)
            return dp[(i, open)]
        return dfs(0, 0)

    def checkValidString(self, s: str) -> bool:
        left_min = 0
        left_max = 0
        for c in s:
            if c == '(':
                left_min += 1
                left_max += 1
            if c == '*':
                left_min -= 1
                left_max += 1
            if c == ')':
                left_min -= 1
                left_max -= 1
            if left_min < 0:
                left_min = 0
            if left_max < 0:
                return False
        return 0 >= left_min and 0 <= left_max


    def checkValidString(self, s: str) -> bool:
        stack = []
        starStack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == '*':
                starStack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
        while stack and starStack:
            if stack.pop() > starStack.pop():
                return False
        return True if not stack else False
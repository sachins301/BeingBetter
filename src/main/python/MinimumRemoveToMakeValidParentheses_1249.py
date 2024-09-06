class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        while(stack):
            s[stack.pop()] = ''
        return ''.join(s)

    def minRemoveToMakeValid_non_optimized(self, s: str) -> str:
        stack = []
        res = ''
        count = 0
        for c in s:
            if c == '(':
                count += 1
                res += c
            elif c == ')':
                if count > 0:
                    res += c
                    count -= 1
            else:
                res += c
        n = len(res)
        for i in range(n-1, -1, -1):
            if count > 0 and res[i] == "(":
                res = res[:i] + res[i+1:]
                count -= 1

        return res


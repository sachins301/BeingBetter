class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        closing = {")" : "(", "}" : "{", "]" : "["}
        for c in s:
            if c in closing.keys():
                if not stack:
                    return False
                opening = stack.pop()
                if opening != closing[c]:
                    return False
            else:
                stack.append(c)

        return False if stack else True
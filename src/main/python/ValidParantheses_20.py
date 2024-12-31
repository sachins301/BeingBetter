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

    def isValid(self, s: str) -> bool:
        pairs = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        return not stack
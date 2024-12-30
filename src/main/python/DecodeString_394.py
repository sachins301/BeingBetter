class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                enc = ''
                while stack and stack[-1] != '[':
                    enc = stack.pop() + enc
                stack.pop()
                count = ''
                while stack and stack[-1] in "0123456789":
                    count = stack.pop() + count
                stack.append(int(count) * enc)
            else:
                stack.append(c)
        return ''.join(stack)
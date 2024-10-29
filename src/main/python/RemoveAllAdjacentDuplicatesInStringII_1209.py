class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                if stack[-1][1] == k-1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([c, 1])
        return ''.join([c*n for c, n in stack])
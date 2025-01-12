class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        open = []
        wildcard = []
        for i, c in enumerate(s):
            if locked[i] == '0':
                wildcard.append(i)
            elif c == '(':
                open.append(i)
            else:
                if open:
                    open.pop()
                elif wildcard:
                    wildcard.pop()
                else:
                    return False
        for i in open[::-1]:
            if wildcard and i < wildcard[-1]:
                wildcard.pop()
            else:
                return False
        return len(wildcard) % 2 == 0
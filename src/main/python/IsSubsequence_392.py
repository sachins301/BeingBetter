class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pos = -1
        for c in s:
            # print(c, t)
            if c not in t:
                return False
            t = t[t.index(c)+1:]
        return True
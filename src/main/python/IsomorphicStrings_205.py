class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping1 = {}
        mapping2 = {}
        for i, c in enumerate(s):
            if (c in mapping1 and t[i] != mapping1[c]) or (t[i] in mapping2 and c != mapping2[t[i]]):
                return False
            else:
                mapping1[c] = t[i]
                mapping2[t[i]] = c
        return True
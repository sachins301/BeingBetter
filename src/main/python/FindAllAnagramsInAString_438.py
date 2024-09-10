class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        if len(s) < n:
            return []
        pCode = [0]*26
        sCode = [0]*26
        a = ord('a')
        res = []
        for i in range(n):
            pCode[ord(p[i]) - a] += 1
            sCode[ord(s[i]) - a] += 1
        if sCode == pCode:
            res.append(0)
        for j in range(n, len(s)):
            i = j - n
            sCode[ord(s[i]) - a] -= 1
            i += 1
            sCode[ord(s[j]) - a] += 1
            if sCode == pCode:
                res.append(i)
        return res


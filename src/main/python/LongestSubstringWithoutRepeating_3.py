class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, res = 0, 0, 0
        seen = set()
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = {}
        l = 0
        r = 0
        res = 0
        while r < len(s):
            if s[r] in visit:
                l = max(l, visit[s[r]] + 1)
            visit[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        return res
class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        s = list(s)
        while l <= r:
            if s[l].lower() in ('a', 'e', 'i', 'o', 'u'):
                while r >= l and s[r].lower() not in ('a', 'e', 'i', 'o', 'u'):
                    r -= 1
                s[l], s[r] = s[r], s[l]
                r -= 1
            l += 1
        return ''.join(s)

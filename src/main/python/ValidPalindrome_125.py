class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        s = s.lower()
        while(l <= r):
            if s[l] < '0' or (s[l] > '9' and s[l] < 'a') or s[l] > 'z':
                l += 1
                continue
            if s[r] < '0' or (s[r] > '9' and s[r] < 'a') or s[r] > 'z':
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
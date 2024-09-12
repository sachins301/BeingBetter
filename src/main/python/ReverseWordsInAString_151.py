class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        return ' '.join(s_list[::-1])
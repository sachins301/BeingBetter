from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre = [0] * (len(s) + 1)
        for start, end, dir in shifts:
            pre[end + 1] += 1 if dir else -1
            pre[start] += -1 if dir else 1
        diff = pre[-1]
        s = [ord(c) - ord('a') for c in s]
        for i in range(len(s) - 1, -1, -1):
            s[i] = (s[i] + diff) % 26
            diff += pre[i]
        s = [chr(n + ord('a')) for n in s]
        return ''.join(s)
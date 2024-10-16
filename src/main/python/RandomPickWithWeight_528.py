from random import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        s = sum(w)
        for i in range(len(w)):
            self.w[i] = w[i] / s
            if i > 0:
                self.w[i] += self.w[i - 1]

    def pickIndex(self) -> int:
        N = random.uniform(0, 1)
        for i, w in enumerate(self.w):
            if N <= w:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ordertable = defaultdict(int)
        order_pos = 0
        for c in order:
            ordertable[c] = order_pos
            order_pos += 1
        print(ordertable)
        res = sorted(s.split(), key = lambda x: ordertable[x])
        return ''.join(res)
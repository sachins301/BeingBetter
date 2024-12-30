from bisect import bisect
from typing import List

from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        sortedlist = SortedList()
        for n in nums[::-1]:
            position = bisect.bisect_left(sortedlist, n)
            res.append(position)
            sortedlist.add(n)
        return res[::-1]

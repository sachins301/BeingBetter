from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dic = set(nums)
        cnt = 0
        res = 0
        for d in dic:
            if d - 1 not in dic:
                cnt = 1
                i = d
                while(i in dic):
                    cnt += 1
                    i += 1
                res = max(res, cnt)
        return res-1
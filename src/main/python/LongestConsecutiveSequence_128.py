from typing import List


class Solution:

    #DP / Memoization
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        numSet = set(nums)
        cache = {}

        def get_streak(n):
            if n not in numSet:
                return 0
            if n in cache:
                return cache[n]
            cache[n] = 1 + get_streak(n + 1)
            return cache[n]

        for n in nums:
            if n - 1 not in numSet:
                res = max(res, get_streak(n))
        return res

    # O(n)
    def longestConsecutive2(self, nums: List[int]) -> int:
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
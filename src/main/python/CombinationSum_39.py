from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(arr, t, lst):
            if t == 0:
                res.append(lst)
                return
            if not arr or t < 0:
                return
            helper(arr, t - arr[0], lst + [arr[0]])
            helper(arr[1:], t, lst)

        helper(candidates, target, [])
        return res
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def helper(i, t, subset):
            if t == 0:
                res.append(subset)
                return
            if i >= len(candidates):
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if candidates[j] <= t:
                    helper(j + 1, t - candidates[j], subset + [candidates[j]])
            return
        helper(0, target, [])
        return res
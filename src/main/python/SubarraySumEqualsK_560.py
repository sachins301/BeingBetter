from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        pre = 0
        seen = {0: 1}
        for num in nums:
            pre += num
            if pre - k in seen:
                res += seen[pre - k]
            if pre in seen:
                seen[pre] += 1
            else:
                seen[pre] = 1
        return res
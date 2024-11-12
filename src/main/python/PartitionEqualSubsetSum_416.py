from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        for n in nums:
            newDp = set()
            for t in dp:
                newDp.add(t + n)
                newDp.add(t)
                if target in newDp:
                    return True
            dp = newDp
        return False
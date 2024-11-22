from typing import List


class Solution:
    # Top down dp
    def jump2(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return float('inf')
            if i in dp:
                return dp[i]
            steps = float('inf')
            for j in range(i+1, min(i + nums[i] + 1, len(nums))):
                steps = min(steps, dfs(j) + 1)
            dp[i] = steps
            return dp[i]
        return dfs(0)

    # bfs
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        res = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res
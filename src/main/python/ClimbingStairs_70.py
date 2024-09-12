class Solution:
    dp = {}
    def climbStairs(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        self.dp[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)
        return self.dp[n]
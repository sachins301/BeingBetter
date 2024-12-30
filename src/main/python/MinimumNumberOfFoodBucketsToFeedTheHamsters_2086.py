class Solution:


    def minimumBuckets(self, hamsters: str) -> int:
        res = 0
        hamsters = list(hamsters)
        for i in range(len(hamsters)):
            if hamsters[i] == '.' or hamsters[i] == 'B':
                continue
            if i > 0 and hamsters[i - 1] == 'B':
                continue
            if i + 1 < len(hamsters) and hamsters[i + 1] == '.':
                hamsters[i + 1] = 'B'
                res += 1
            elif i > 0 and hamsters[i - 1] == '.':
                hamsters[i - 1] = 'B'
                res += 1
            else:
                return -1
        return res

    def minimumBuckets(self, hamsters: str) -> int:
        res = 0
        dp = {}
        def dfs(i):
            if i >= len(hamsters):
                return 0
            if i in dp:
                return dp[i]
            if hamsters[i] == ".":
                return dfs(i + 1)
            res = float('inf')
            if i - 1 >= 0 and hamsters[i - 1] == ".":
                res = dfs(i + 1) + 1

            if i + 1 < len(hamsters) and hamsters[i + 1] == ".":
                res = min(res, dfs(i + 3) + 1)
            dp[i] = res
            return res

        res = dfs(0)
        return res if res != float('inf') else -1
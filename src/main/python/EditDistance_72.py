class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1)):
            dp[i][-1] = len(word1) - i
        for j in range(len(word2)):
            dp[-1][j] = len(word2) - j
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        # for line in dp:
        #     print(line)
        return dp[0][0]


    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def dfs(i, k):
            if i == len(word1):
                return len(word2) - k
            if k == len(word2):
                return len(word1) - i
            if (i, k) in dp:
                return dp[(i, k)]
            if word1[i] == word2[k]:
                dp[(i, k)] = dfs(i + 1, k + 1)
            else:
                dp[(i, k)] = min(dfs(i + 1, k), dfs(i, k + 1), dfs(i + 1, k + 1)) + 1
            return dp[(i, k)]
        return dfs(0, 0)
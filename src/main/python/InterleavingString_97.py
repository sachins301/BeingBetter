class Solution:


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        def helper(i, j):
            if i == len(s1) and j == len(s2) and i + j == len(s3):
                return True
            if i + j >= len(s3):
                dp[(i, j)] = False
                return False
            if (i, j) in dp:
                return dp[(i, j)]
            if i < len(s1) and s1[i] == s3[i + j] and helper(i + 1, j):
                return True
            print(i, j)
            if j < len(s2) and s2[j] == s3[i + j] and helper(i, j + 1):
                return True
            dp[(i, j)] = False
            return False
        return helper(0, 0)


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[-1][-1] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        def helper(i, j, k):
            if k == len(s3):
                if i == len(s1) and j == len(s2):
                    return True
                else:
                    return False
            if (i, j, k) in dp:
                return dp[(i, j, k)]
            if i < len(s1) and s1[i] == s3[k]:
                if helper(i + 1, j, k + 1):
                    dp[(i, j, k)] = True
            if (i, j, k) not in dp and j < len(s2) and s2[j] == s3[k]:
                if helper(i, j + 1, k + 1):
                    dp[(i, j, k)] = True
            if (i, j, k) not in dp:
                dp[(i, j, k)] = False
            return dp[(i, j, k)]

        return helper(0, 0, 0)
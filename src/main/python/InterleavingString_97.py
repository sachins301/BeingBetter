class Solution:
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
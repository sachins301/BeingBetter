from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        '''
        dog(10)  ""(0)
        '''

        dp = {}
        def dfs(i, letters):
            if i == len(words):
                return 0
            temp = letters.copy()
            res = 0
            for c in words[i]:
                if c not in temp:
                    return dfs(i + 1, letters)
                temp.remove(c)
                res += score[ord(c) - ord('a')]
            res = max(res + dfs(i + 1, temp), dfs(i + 1, letters))
            return res
        return dfs(0, letters)
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def helper(i, curr):
            if i == len(digits):
                res.append(curr)
                return
            for c in digitToChar[digits[i]]:
                helper(i + 1, curr + c)
            return
        if digits:
            helper(0, "")
        return res
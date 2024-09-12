from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        word_list = text.split()
        for i, word in enumerate(word_list):
            if i + 1 < len(word_list) and i + 2 < len(word_list) and word == first and word_list[i + 1] == second:
                res.append(word_list[i + 2])

        return res

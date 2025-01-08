from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i, word in enumerate(words):
            if word in ' '.join(words[:i]) or word in ' '.join(words[i+1:]):
                # print(word, ' '.join(words[:i]), ' '.join(words[i+1:]))
                res.append(word)

        return res
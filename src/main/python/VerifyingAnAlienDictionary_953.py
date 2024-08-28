class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        res = []
        for word in words:
            score = []
            for c in word:
                score.append(order.index(c))
            res.append(score)
        last = []
        for s in res:
            if s < last:
                return False
            last = s

        return True
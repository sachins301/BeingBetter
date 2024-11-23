from collections import Counter
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num]:
                for n in range(num, num + groupSize):
                    if not count[n]:
                        return False
                    count[n] -= 1
        return True
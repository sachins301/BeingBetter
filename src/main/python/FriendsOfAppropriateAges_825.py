from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        res = 0
        count = [0] * 121
        for age in ages:
            count[age] += 1
        for agei, cnt1 in enumerate(count):
            for agej, cnt2 in enumerate(count):
                if agej <= 0.5 * agei + 7 or agej > agei or (agej > 100 and agei < 100):
                    continue
                res += cnt1 * cnt2
                if agei == agej:
                    res -= cnt1

        return res
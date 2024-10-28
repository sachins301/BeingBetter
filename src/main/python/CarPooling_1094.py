from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timetable = []
        curr_passengers = 0
        for trip in trips:
            timetable.append((trip[0], trip[1]))
            timetable.append((-trip[0], trip[2]))
        timetable.sort(key = lambda x: (x[1], x[0]))
        for trip in timetable:
            curr_passengers += trip[0]
            if curr_passengers > capacity or curr_passengers < 0:
                return False
        return True
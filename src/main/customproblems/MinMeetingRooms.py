"""
1. Interval Scheduling and Overlaps
Problem: Given a list of meeting time intervals, determine the minimum number of conference rooms required to schedule all meetings.

Solution: To solve this, we can use a sweep line technique by treating meeting start and end times as events. We
increment the room count when a meeting starts and decrement when it ends. The maximum number of overlapping events
at any point gives the number of rooms required."""

def minMeetingRooms(intervals):
    if not intervals:
        return 0

    # Separate start and end times, and sort them
    start_times = sorted([i[0] for i in intervals])
    end_times = sorted([i[1] for i in intervals])

    rooms = 0
    end_ptr = 0

    # Iterate through start times and use end_ptr to track end times
    for start in start_times:
        if start >= end_times[end_ptr]:  # A room is freed up
            end_ptr += 1
        else:  # A new room is needed
            rooms += 1

    return rooms

# Example usage:
intervals = [[0, 30], [5, 10], [15, 20], [20, 30]]
print(minMeetingRooms(intervals))  # Output: 2
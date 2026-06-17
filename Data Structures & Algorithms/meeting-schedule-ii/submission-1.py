"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

'''
For each new meeting that starts do meetingRooms += 1, when any meeting ends,
subtract 1. Use two pointers pointing to sorted starts start and sorted ends'
start. if start[s] < end[e] meaning curr new meeting start is before prev e ends
so we increment meetingRooms by 1, else we decrement meetingRooms coz new start is
after prev ended, so that room is freed. increment e by 1 too

Time: O(n log n)
Space: O(n)
'''
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        # meeting start time pointer
        s = 0
        # meeting end time pointer
        e = 0
        
        res = 0
        meetingRooms = 0
        
        while s < len(intervals):
            # if new meeting starts before prev one ends
            # we need another meeting room
            if start[s] < end[e]:
                meetingRooms += 1
                s += 1
            else:
                # else new meeting starts after current one ends
                # so we don't need the current meeting's room anymore
                e += 1
                meetingRooms -= 1
            res = max(res, meetingRooms)

        return res

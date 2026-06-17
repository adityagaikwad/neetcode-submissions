'''
Binary search insertion then linear merge

Binary search locates the position where newInterval's start fits among the sorted start
times, then inserts it there. After insertion the list is sorted by start but may contain
new overlaps. A single left-to-right pass resolves them: each interval either opens a
fresh non-overlapping range or extends the last range's end if they overlap.

Note: Can also just append to end, sort arr and then do merge intervals

Time: O(n)
    insert() shifts up to n elements; the O(log n) binary search is dominated by that shift.
    The merge pass visits every interval once.
Space: O(n)
    result list holds at most n + 1 intervals
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        n = len(intervals)
        # binary search to find idx where new interval's start fits properly
        target = newInterval[0]
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2

            if intervals[mid][0] < target:
                # will insert at mid + 1 or higher
                left = mid + 1
            else:
                # if mid is greater we cannot insert at mid, do -1
                right = mid - 1

        # insert new interval at correct pos by startTime
        intervals.insert(left, newInterval)
        
        # merge intervals if needed
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res

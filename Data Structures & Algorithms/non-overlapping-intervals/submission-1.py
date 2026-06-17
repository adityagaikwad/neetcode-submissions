class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        O(nlogn)
        '''
        count = 0
        intervals.sort(key = lambda x: x[0])

        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                count += 1
                # to find overlapping with the smaller
                # of the two intervals next time
                # we remove the larger interval to minimize count
                prevEnd = min(end, prevEnd)

        return count

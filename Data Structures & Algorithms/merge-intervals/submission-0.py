class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals by their starting time
        intervals = sorted(intervals, key=lambda x: x[0])
        # initialize an empty list to store the non-overlapping intervals
        merged = []
        # iterate through the intervals
        for interval in intervals:
            # if the list of non-overlapping intervals is empty or the current interval does not overlap with the previous one
            if not merged or interval[0] > merged[-1][1]:
                # add the current interval to the list
                merged.append(interval)
            else:
                # otherwise, merge the current interval with the previous one
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
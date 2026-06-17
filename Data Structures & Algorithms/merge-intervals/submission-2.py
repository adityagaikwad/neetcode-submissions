'''
Time: O(n logn)
Space: O(n)/O(1) for merged/intervals arrs
'''
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

'''
Greedy with auxiliary reach array

For each possible start index, record the farthest end of any interval beginning there.
Then scan left to right, maintaining curr_merged_interval_end: the farthest index the
current merged interval must cover before it can be closed. Whenever a new start is
encountered, curr_merged_interval_end is extended if that interval reaches further right.
The merged interval closes exactly when the scan index catches up to curr_merged_interval_end,
guaranteeing no overlapping interval was skipped.

reach[i] = farthest end + 1 of any interval starting at i; 0 if no interval starts there.
curr_merged_interval_end = the current merged interval stays open until the scan index reaches this value.

Time: O(n + M)
    n intervals fill reach in O(n); the scan covers M positions where M = max start value
Space: O(M)
    reach array of size max_start + 1; M is bounded by the largest interval start value
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_start = max(interval[0] for interval in intervals)

        # store end+1 so that 0 can unambiguously mean "no interval starts here"
        reach = [0] * (max_start + 1)
        for start, end in intervals:
            # store farthest end for each start across intervals
            reach[start] = max(end + 1, reach[start])

        merged = []
        curr_merged_interval_end = -1
        merge_start = -1
        for i in range(len(reach)):
            if reach[i] != 0:
                if merge_start == -1:
                    merge_start = i
                # convert back from end+1 to actual end before comparing
                curr_merged_interval_end = max(reach[i] - 1, curr_merged_interval_end)
            # curr intervals overlap has reached end
            if curr_merged_interval_end == i:
                merged.append([merge_start, curr_merged_interval_end])
                curr_merged_interval_end = -1
                merge_start = -1

        if merge_start != -1:
            merged.append([merge_start, curr_merged_interval_end])

        return merged

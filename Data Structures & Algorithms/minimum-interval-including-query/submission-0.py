class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''
        Min heap
        Time: O(nlogn + mlogm)
            n = len intervals
            m = len queries
        Space: O(n + m)
            n for min heap
            m for res dict
        '''
        # Step 1: Sort the intervals based on their start point
        intervals.sort()

        # Min heap to store intervals that cover the current query
        # Each element in the heap is a tuple: (interval_length, right_endpoint)
        minHeap = []

        # Dictionary to store the result for each query
        res = {}

        # Pointer to track which intervals have been added to the heap
        i = 0

        # Step 2: Sort the queries so we can process them in increasing order
        for q in sorted(queries):
            # Step 3: Add all intervals that start <= q to the heap
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))  # push (interval length, end)
                i += 1

            # Step 4: Remove intervals from the heap that end before the query point
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # Step 5: The top of the heap is the smallest interval that contains q
            # If the heap is empty, no interval covers q
            res[q] = minHeap[0][0] if minHeap else -1

        # Step 6: Return results in the original order of queries
        return [res[q] for q in queries]
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        max_heap = []

        # add numbers from first window to max heap
        for i in range(k):
            heapq.heappush(max_heap, (-nums[i], i))
        
        # top of heap is max of first sliding window
        res.append(-max_heap[0][0])
        
        # move window to right by 1
        for i in range(k, len(nums)):
            # add new number to sliding window
            # NOTE: Now len(window) = k + 1
            heapq.heappush(max_heap, (-nums[i], i))

            # remove numbers which are outside of the window
            # from the heap. i.e while heap number index <
            # i - k + 1 (start of window index)
            startOfWindowIndex = i - k + 1
            while max_heap[0][1] < startOfWindowIndex:
                heapq.heappop(max_heap)

            # after removing all out of window numbers,
            # heap top is max of current window
            res.append(-max_heap[0][0])
        
        return res
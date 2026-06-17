import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Heap approach
        
        Time complexity: O(nlogk)
        Space complexity: O(n)
            If we consider res arr
            Otherwise O(k) for heap
        '''
        # res = []

        # max_heap = []

        # # add numbers from first window to max heap
        # for i in range(k):
        #     heapq.heappush(max_heap, (-nums[i], i))
        
        # # top of heap is max of first sliding window
        # res.append(-max_heap[0][0])
        
        # # move window to right by 1
        # for i in range(k, len(nums)):
        #     # add new number to sliding window
        #     # NOTE: Now len(window) = k + 1
        #     heapq.heappush(max_heap, (-nums[i], i))

        #     # remove numbers which are outside of the window
        #     # from the heap. i.e while heap number index <
        #     # i - k + 1 (start of window index)
        #     startOfWindowIndex = i - k + 1
        #     while max_heap[0][1] < startOfWindowIndex:
        #         heapq.heappop(max_heap)

        #     # after removing all out of window numbers,
        #     # heap top is max of current window
        #     res.append(-max_heap[0][0])
        
        # return res

        '''
        Deque approach
        
        Time complexity: O(n)
        Space complexity: O(n)
        '''
        res = []

        # this queue will hold indexes of
        # (elements in decreasing order in active window)
        q = deque()
        l = r = 0

        for i in range(len(nums)):
            # Remove elements from deque if
            # they are out of the current window
            if q and q[0] < i - k + 1:
                q.popleft()

            # remove elements from queue which are smaller
            # than current element, since we won't need them
            # for max value ever in current or future windows
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            
            # add current element to the end of queue
            q.append(i)

            # if first sliding window is processed
            if i >= k - 1:
                # q[0] i.e front of queue will have max value
                res.append(nums[q[0]])
        
        return res
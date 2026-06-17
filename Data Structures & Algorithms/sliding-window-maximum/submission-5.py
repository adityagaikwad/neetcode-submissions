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

        Instead of a heap, we maintain a deque of indices whose corresponding values
        are in strictly decreasing order. This means the front always holds the index
        of the current window's maximum, and we never need to scan the whole window.

        Deque invariant:
        - Front (q[0]): index of the largest element in the current window.
        - Back  (q[-1]): index of the most recently added element, which is the
                        smallest in the deque.

        When we advance to index i:
        1. Evict from the front if that index has fallen outside the window.
        2. Pop from the back any indices whose values are <= nums[i], because a
            smaller element that arrived earlier can never be the window max while
            the current (larger) element is still in the window.
        3. Append i to the back. nums[i] would be in correct pos coz we removed nums
        smaller than nums[i] from queue
        4. Once i >= k-1 the first full window is formed, so nums[q[0]] is the max.

        Time complexity: O(n) — each index is pushed and popped at most once.
        Space complexity: O(k) — the deque holds at most k indices at any time.
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
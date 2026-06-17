import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        heap = []

        # max heap
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        
        # heap top has first window's max element
        res = [-heap[0][0]]
        for i in range(k, n):
            # remove out of window elements from heap top
            while heap and heap[0][1] <= i - k:
                heapq.heappop(heap)
            
            heapq.heappush(heap, (-nums[i], i))

            res.append(-heap[0][0])
        
        return res


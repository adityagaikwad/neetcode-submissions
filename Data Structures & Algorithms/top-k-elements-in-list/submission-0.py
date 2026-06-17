from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounts = Counter(nums)

        heap = []
        for num in numCounts.keys():
            heapq.heappush(heap, (numCounts[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for _, num in heap]
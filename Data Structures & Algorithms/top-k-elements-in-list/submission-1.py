from collections import Counter
import heapq

class Solution:
    '''
    Min heap of size k to store top counts

    Time Complexity: O (n * log k)
    Space Complexity: O(n + k)

    n = len(nums)
    k = num of top frequent elements
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res

from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for x, y in points:
            distance = x**2 + y**2
            heappush(maxHeap, (-distance, x, y))

            if len(maxHeap) > k:
                heappop(maxHeap)
        
        res = []
        for _ in range(len(maxHeap)):
            distance, x, y = heappop(maxHeap)
            res.append([x, y])
        
        return res
        

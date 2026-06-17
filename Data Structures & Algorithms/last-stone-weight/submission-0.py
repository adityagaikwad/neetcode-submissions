class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        
        while len(maxHeap) > 1:
            x = abs(heapq.heappop(maxHeap))
            y = abs(heapq.heappop(maxHeap))

            if x == y:
                continue
            
            newWeight = abs(x - y)
            heapq.heappush(maxHeap, -newWeight)
        
        return abs(maxHeap[0]) if maxHeap else 0

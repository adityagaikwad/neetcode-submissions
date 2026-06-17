class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k

        for num in nums[:k]:
            heapq.heappush(self.heap, num)

        for num in nums[k:]:
            heapq.heappush(self.heap, num)
            # pop smaller element
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]

from heapq import heappop, heappush

class MedianFinder:
    '''
    We use two heaps
    For ex. [1, 3, 2, 5, 4, 6]
    heap1 = [3, 2, 1] heap2 = [4, 5, 6]
    
    In heap1 largest element in left sorted is at top
    In heap2 smallest element in right sorted is at top

    So if len(heap1) > len(heap2): return heap1[0] (largest in left half)
    if len(heap1) < len(heap2): return heap2[0] (smallest in right half)
    if equal: return (heap1[0] + heap2[0]) / 2
    '''
    def __init__(self):
        self.leftMaxHeap = []
        self.rightMinHeap = []

    def addNum(self, num: int) -> None:
        if self.rightMinHeap and num > self.rightMinHeap[0]:
            # min heap so add normally
            heappush(self.rightMinHeap, num)
        else:
            # max heap so negate and add
            heappush(self.leftMaxHeap, -num)

        # if difference is of two or more elements
        if len(self.leftMaxHeap) > len(self.rightMinHeap) + 1:
            # move from left minHeap to right maxHeap
            val = -heappop(self.leftMaxHeap)
            heappush(self.rightMinHeap, val)
        elif len(self.rightMinHeap) > len(self.leftMaxHeap) + 1:
            # move from right maxHeap to left minHeap
            val = heappop(self.rightMinHeap)
            heappush(self.leftMaxHeap, -val)

    def findMedian(self) -> float:
        if len(self.leftMaxHeap) > len(self.rightMinHeap):
            return -1 * self.leftMaxHeap[0]
        elif len(self.rightMinHeap) > len(self.leftMaxHeap):
            return self.rightMinHeap[0]
        else:
            # both have equal elements
            # median is (num1+num2)/2
            return (-1 * self.leftMaxHeap[0] + self.rightMinHeap[0]) / 2.0
        
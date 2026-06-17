'''
Max heap approach

Time: O(n logn)
Space: O(n)
'''
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

'''
Bucket sort approach
Only works when w is not too high

Build a frequency array count where count[w] stores the number of stones with weight w.
Scan from heavy = max_weight downward, skipping weights with even counts since those stones
fully cancel each other out. When an odd-count weight is found, locate the next lighter stone
(candidate) by scanning downward from the light upper bound and smash the two: decrement both
counts, add a new stone at count[heavy - light], then reset heavy to max(heavy - light, light).
The light variable caches the last confirmed lighter stone position so the scan never revisits
weights that are already exhausted or fully paired.

Time: O(n + w)
    n = len(stones)
    w = max(stones)

    n for getting max
    w for iterating bucket worst case fully

Space: O(w)
    for bucket
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_weight = max(stones)
        
        bucket = [0] * (max_weight + 1)
        for stone in stones:
            bucket[stone] += 1

        heavy = max_weight  # heaviest weight currently under consideration
        light = max_weight  # upper bound for searching the next lighter stone

        while heavy > 0:
            if bucket[heavy] % 2 == 0:
                # even bucket: all stones at this weight cancel each other out
                heavy -= 1
                continue

            # one leftover stone at `heavy`; find the next lighter stone to smash it with
            # start from `light` (not heavy-1) because weights above it are already exhausted
            # light could still be at max_weight, while heavy was subtracted
            candidate = min(heavy - 1, light)
            while candidate > 0 and bucket[candidate] == 0:
                candidate -= 1

            if candidate == 0:
                return heavy  # no lighter stone exists; `heavy` is the last stone

            light = candidate
            # pop one of both from their buckets
            bucket[heavy] -= 1
            bucket[light] -= 1
            bucket[heavy - light] += 1         # new stone produced by the smash
            heavy = max(heavy - light, light)  # new heaviest possible stone

        return heavy
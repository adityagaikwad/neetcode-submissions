'''
Brute force: try every k from 1 to max(piles), return the first one
where total hours <= h. That's O(n * m) — too slow when piles are large.

Optimization: notice that as k increases, total hours needed only decreases
(or stays the same). So the valid k values look like: 
too slow, too slow, ..., OK, OK, OK, OK]
                         ^
                         first valid k = answer

Any time you have a sorted yes/no boundary like this, binary search finds it
in O(log m) instead of scanning every value.

Binary search on the answer (eating rate k), not on the input array.

Key insight: if rate k lets Koko finish in time, any rate > k also works.
This monotonic property means we can binary search on k directly.

Search space: k=1 (slowest possible) to k=max(piles) (finishes any pile in 1 hour,
so never needs more than len(piles) hours, which is always <= h).

For each candidate k, compute total hours needed as sum of ceil(pile/k)
across all piles. If that fits within h, k is a valid answer, 
record it and search left for something smaller. If it exceeds h,
k is too slow — search right.

Time: O(n log m), n = len(piles), m = max(piles)
Space: O(1)
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK = 1
        res = maxK = max(piles)

        while minK <= maxK:
            k = (minK + maxK) // 2

            totalTimeReq = 0
            for bananas in piles:
                totalTimeReq += math.ceil(bananas/k)
            
            if totalTimeReq <= h:
                res = k
                maxK = k - 1
            else:
                minK = k + 1
        
        return res
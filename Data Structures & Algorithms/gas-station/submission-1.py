
'''
Greedy scan

If total gas < total cost, completing the circuit is impossible regardless of
where you start. Otherwise, exactly one valid starting point exists.

The key insight: if the running surplus goes negative at station i, then no
station in [start..i] can be the answer. Any start within that window would
also run dry at i, because it would have had less gas available at each step
(it skipped the surplus accumulated before its own index). So the entire
window is eliminated and we try i+1 next.

Because the problem guarantees at most one solution, whichever candidate
survives to the end of the scan is correct.

total = running gas surplus from the current start candidate
start = index of the current candidate starting station

Time: O(n)
    Single pass through both arrays (sum() calls are each O(n) but constant factor)
Space: O(1)
    No auxiliary data structures; only two scalar variables
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                # every station in [start..i] is also invalid; skip the whole window
                start = i + 1

        return start


'''
O(n^2) solution
'''
# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         n = len(gas)

#         for i in range(n):
#             tank = gas[i] - cost[i]
#             if tank < 0:
#                 continue

#             j = (i + 1) % n
#             while j != i:
#                 tank += gas[j]
#                 tank -= cost[j]
#                 if tank < 0:
#                     break
#                 j += 1
#                 j %= n

#             if j == i:
#                 return i
#         return -1

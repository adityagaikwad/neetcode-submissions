from collections import defaultdict
from heapq import heappush, heappop
from typing import List


'''
Bellman-Ford

Have a prices arr which tracks curr lowest price to reach airport i
k stops meaning we can take k + 1 flights, or have k + 1 edges traversed
from src to dest. Init prices arr to all float(inf) except src.

So do for loop k + 1 times, with prices[src] = 0 ensuring we start exploring
airports via edges connected to src.

So at iteration 1 we find cheapest prices to reach all airports at 1 flight away
from src, so at k + 1 flights we can ensure that prices arr has cheapest by taking
at most k + 1 flights or k stops.

Time: O(k * m)
    k+1 passes, each iterating over all m flights; no heap overhead
    n = number of airports (nodes)
    m = number of flights (edges)
Space: O(n)
    Two price arrays of size n, swapped each pass
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # tracks curr min price to reach airport i
        prices = [float("inf")] * n
        # ensures that all edges originate from src
        prices[src] = 0
        
        # k stops = k+1 flights, so run k+1 relaxation passes
        for i in range(k + 1):
            # freeze the previous pass so this pass can only add one new flight
            tmpPrices = prices.copy()

            for s, d, p in flights:
                # node not yet reachable, no point checking its edges
                if prices[s] == float("inf"):
                    continue
                # cost to reach s + cost from s to d if lower than prev
                # update tmpPrices[d] with new lower price
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            
            prices = tmpPrices

        return -1 if prices[dst] == float("inf") else prices[dst]


'''
Modified Dijkstra (2D state space)

Standard Dijkstra cannot stop at the first visit to a node here, because a
cheaper path might exist that uses more flights. The fix is to track state as
(node, flights_taken) and allow a node to be revisited at different flight
counts. dist[node][f] prunes any state that has already been reached cheaper
at the same flight count.

The first time dst is popped from the heap is still guaranteed optimal, since
the heap orders by cost.

dist[node][f] = minimum cost to reach node using exactly f flights

Time: O(k * m * log(n * k))
    Up to m edges relaxed per flight level, each heap op costs log(n*k)
Space: O(n * k + m)
    dist table is n*(k+2), heap holds at most n*(k+1) entries, adj stores m edges
'''
# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         adj = defaultdict(list)

#         for u, v, cost in flights:
#             adj[u].append((v, cost))

#         # We can take at most k + 1 flights (which means k stops)
#         max_flights = k + 1
#         # dist[node][flights_taken] = min cost to reach 'node' using 'flights_taken' flights
#         # k + 2 coz we can do checks for visited[k + 1] at most
#         dist = [[float('inf')] * (max_flights + 1) for _ in range(n)]
#         dist[src][0] = 0

#         # (cost so far, current node, flights taken so far)
#         minHeap = [(0, src, 0)]

#         while minHeap:
#             currCost, node, flights_taken = heappop(minHeap)

#             # first time we reach dst will always be shortest
#             if node == dst:
#                 return currCost

#             if flights_taken == max_flights:
#                 continue

#             for nei, price in adj[node]:
#                 newCost = currCost + price
#                 # If the new cost with 'flights_taken + 1' is less than
#                 # the current cost to reach 'dest' with 'stops + 1', add to minHeap
#                 if newCost < dist[nei][flights_taken + 1]:
#                     dist[nei][flights_taken + 1] = newCost
#                     heappush(minHeap, (newCost, nei, flights_taken + 1))

#         return -1
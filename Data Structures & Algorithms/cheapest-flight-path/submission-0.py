from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, cost in flights:
            adj[u].append((v, cost))

        # We can take at most k + 1 flights (which means k stops)
        # dist[node][flights_taken] = min cost to reach 'node' using 'flights_taken' flights
        max_flights = k + 1
        dist = [[float('inf')] * (max_flights + 1) for _ in range(n)]
        dist[src][0] = 0

        # (cost so far, current node, flights taken so far)
        minHeap = [(0, src, 0)]

        while minHeap:
            currCost, node, flights_taken = heapq.heappop(minHeap)

            if node == dst:
                return currCost

            if flights_taken == max_flights:
                continue

            for nei, price in adj[node]:
                newCost = currCost + price
                if newCost < dist[nei][flights_taken + 1]:
                    dist[nei][flights_taken + 1] = newCost
                    heapq.heappush(minHeap, (newCost, nei, flights_taken + 1))

        return -1
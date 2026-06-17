from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        Time: O((n + m) * k)
            Where n is the number of cities
            m is the number of flights and 
            k is the number of stops

            Each city can be processed up to k + 1 times (for each possible stop count).
            For each such visit, you may explore its outgoing flights (edges).
            You're essentially traversing a layered graph (like BFS), where the depth is up to k.

        Space: O(n * k + m)
            adj: O(m)
            dist: O(n * (k + 2))
            minHeap: O(n * (k + 1)) in worst case
        '''
        adj = defaultdict(list)

        for u, v, cost in flights:
            # (destination, cost to reach destination)
            adj[u].append((v, cost))

        # We can take at most k + 1 flights (which means k stops)
        # dist[node][flights_taken] = min cost to reach 'node' using 'flights_taken' flights
        max_flights = k + 1
        # k + 2 coz we can do checks for visited[k + 1] at most
        # dist[node][flights_taken] = minimum cost to reach 'node' using exactly 'flights_taken' flights
        dist = [[float('inf')] * (max_flights + 1) for _ in range(n)]
        dist[src][0] = 0

        # (cost so far, current node, flights taken so far)
        minHeap = [(0, src, 0)]

        while minHeap:
            currCost, node, flights_taken = heapq.heappop(minHeap)

            # first time we reach dst will always be shortest
            if node == dst:
                return currCost

            if flights_taken == max_flights:
                continue

            for nei, price in adj[node]:
                newCost = currCost + price
                # If the new cost with 'flights_taken + 1' is less than
                # the current cost to reach 'dest' with 'stops + 1', add to minHeap
                if newCost < dist[nei][flights_taken + 1]:
                    dist[nei][flights_taken + 1] = newCost
                    heapq.heappush(minHeap, (newCost, nei, flights_taken + 1))

        return -1

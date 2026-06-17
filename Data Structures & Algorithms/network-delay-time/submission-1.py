from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        In this implementation of Dijkstra’s algorithm, we use a min-heap to always process 
        the next closest unvisited node by signal time. For each node, we update its 
        neighbors’ tentative distances and add them to the heap. Once all nodes are 
        visited, the last distance popped (i.e., distanceSoFar) will be the maximum delay 
        to reach the farthest node from the source k.

        Djikstra's shortest path algo
        Time: O(E log V)
            Iterate all edges and add V^2 nodes to minHeap
            E = V^2 coz for every node, if its connected to every other node there's V*V-1 edges.
            logV^2 = logV
        Space: O(E + V)
            E for edges adjacency list and V for visited
        '''
        edges = collections.defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t))
        
        # (distanceToNode, node)
        minHeap = [(0, k)]
        visited = set()

        distanceSoFar = 0

        while minHeap:
            dist, node = heappop(minHeap)

            # only visit node once to ensure shortest distance
            if node in visited:
                continue

            # update curr min shortest distance, on last node this will be updated once
            # it will be the total distance to reach last node from node k
            distanceSoFar = dist
            visited.add(node)

            for neighbor, weight in edges[node]:
                if neighbor not in visited:
                    heappush(minHeap, (dist + weight, neighbor))

        return distanceSoFar if len(visited) == n else -1

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        Djikstra's shortest path algo
        Time: O(E log V)
        Space: O(E + V)
        '''
        edges = collections.defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t))
        
        # (distanceToNode, node)
        minHeap = [(0, k)]
        visited = set()

        distanceSoFar = 0
        while minHeap:
            weight1, node1 = heapq.heappop(minHeap)

            if node1 in visited:
                continue

            distanceSoFar = weight1
            visited.add(node1)

            for node2, weight2 in edges[node1]:
                if node2 not in visited:
                    heapq.heappush(minHeap, (weight1 + weight2, node2))
        
        return distanceSoFar if len(visited) == n else -1

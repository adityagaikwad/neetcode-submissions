from collections import defaultdict

'''
DFS with visited set
Build graph[start].append(end) and graph[end].append(start) using edges

Then start dfs from any node, say node 0 and visit each node and its neighbors
If we get to same visited node again its a cycle, return False

Time complexity: O(V+E)
    Each node and edge visited once
Space complexity: O(V+E)
    Graph size

But E <= V so O(V) or O(n)
'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A fully connected tree has n - 1 edges, so def not a tree if greater
        if len(edges) > (n - 1):
            return False
            
        graph = defaultdict(list)

        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor != prev:
                    if not dfs(neighbor, node):
                        return False

            return True
        
        # start with node 0, can be any node though
        # only if we got to all nodes is it a valid tree
        return dfs(0, -1) and len(visited) == n

from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        Time complexity: O(V+E)
        Space complexity: O(V+E)

        But E <= V so O(V) or O(n)
        '''
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
                # to avoid false positives in cycle detection
                # since 1 -> 2 then 2 -> 1 can be fake cycle
                if neighbor != prev:
                    # cycle found
                    if not dfs(neighbor, node):
                        return False

            return True

        return dfs(0, -1) and len(visited) == n    
        
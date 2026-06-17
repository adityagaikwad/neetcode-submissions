class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjencyList = [[] for _ in range(n)]
        visited = set()

        for u, v in edges:
            adjencyList[u].append(v)
            adjencyList[v].append(u)

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for neighbor in adjencyList[node]:
                dfs(neighbor)
        
        res = 0
        # for each component start dfs if not in visited
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1
        
        return res

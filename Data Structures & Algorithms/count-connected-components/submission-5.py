'''
DFS

O(E + V) for time and space
'''
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

'''
Union find

O(E + V) for time and space
'''
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(node):
            curr = node

            # till we don't find the root of the component
            while curr != parent[curr]:
                # path compression to avoid recursive checks
                # in the future finds
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]
            
            return curr
        
        def union(n1, n2):
            parent1, parent2 = find(n1), find(n2)

            # if the parents are the same, no need to merge
            if parent1 == parent2:
                return False

            # merge n2 into n1
            if rank[parent1] > rank[parent2]:
                '''
                IMP: node2's parent's parent is now node1
                '''
                parent[parent2] = n1
                # increase rank of n1 by 1 since we added one more node to it
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = n2
                rank[parent2] += rank[parent1]
            
            return True
        
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        res = n
        for n1, n2 in edges:
            if union(n1, n2):
                res -= 1
        
        return res
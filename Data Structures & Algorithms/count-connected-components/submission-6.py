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
# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         parent = [i for i in range(n)]
#         # rank = size of component i with root parent as i
#         rank = [1 for i in range(n)]
        
#         # find the root parent of passed node from connected component/graph
#         def find(node):
#             curr = node

#             # for connected non parent nodes, curr = parent[curr]
#             # means that this is the topmost/top parent node in that component
#             while curr != parent[curr]:
#                 # skipping ahead a few nodes to make it faster
#                 # also ensuring future checks are faster, by updating parents
#                 # its called path compression 
#                 parent[curr] = parent[parent[curr]]
#                 curr = parent[curr]
            
#             return curr

#         def union(n1, n2):
#             parent1 = find(n1)
#             parent2 = find(n2)

#             # if the parents are the same, they're already merged/connected
#             # no need to union rn
#             if parent1 == parent2:
#                 return False

#             # merge n2 into n1
#             if rank[parent1] > rank[parent2]:
#                 '''
#                 IMP: node2's parent's parent is now parent1
#                 '''
#                 parent[parent2] = parent1
#                 # increase rank of n1 by rank[n2] since we added one more node to it
#                 rank[parent1] += rank[parent2]
#             else:
#                 parent[parent1] = parent2
#                 rank[parent2] += rank[parent1]

#             return True

#         res = n
#         for n1, n2 in edges:
#             # n1, n2 belong to same component, so reduce res by 1
#             if union(n1, n2):
#                 res -= 1

#         return res

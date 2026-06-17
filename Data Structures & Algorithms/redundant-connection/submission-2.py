'''
Use union find on non-connected vertices by iterating edges to join the edges
When we join normally it will form a graph. When we try to join two nodes which
are already connected, that's when joining these two would lead to a cycle.
This is the edge which can be removed

It's the latest edge by default

Time: O(V + E * alpha(V)) for time and space, here E = V
    We require O(V) time to initialize the DSU (Disjoint Set Union)/Union Find arrays
    
    Iterating over every edge requires O(E) operations, and for every operation,
    we are performing the union method which is O(Alpha(V)) O(α(V)), where α(V)
    is the inverse Ackermann function.
    α(n) < 5 for any practical input size, so it's effectively O(1).

Space: O(V)
    For the arrays
'''
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # find the root parent of passed node from connected component/graph
        def find(node):
            curr = node

            # for connected non parent nodes, curr = parent[curr]
            # means that this is the topmost/top parent node in that component
            while curr != parent[curr]:
                # skipping ahead a few nodes to make it faster
                # also ensuring future checks are faster, by updating parents
                # its called path compression 
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]
            
            return curr

        def union(n1, n2):
            parent1 = find(n1)
            parent2 = find(n2)

            # if the parents are the same, they're already merged/connected
            # no need to union rn
            if parent1 == parent2:
                return False

            # merge n2 into n1
            if rank[parent1] > rank[parent2]:
                '''
                IMP: node2's parent's parent is now parent1
                '''
                parent[parent2] = parent1
                # increase rank of n1 by rank[n2] since we added one more node to it
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]

            return True
        
        # in a fully connected tree, num vertices = num edges + 1
        # in a fully connected tree + 1 edge, num vertices = num edges
        numVertices = len(edges)

        # 1 indexed vertices
        parent = [i for i in range(numVertices + 1)]
        rank = [1 for _ in range(numVertices + 1)]

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
        
        return []

'''
DFS

Build an adjacency list from all edges, then run a single DFS from node 1.
When DFS hits a node that is already visited, that node is the start of the cycle.

During backtracking, every node on the return path back to cycleStart is added to
the cycle set coz all these nodes were in the cycle too.

Once backtracking reaches cycleStart itself, cycleStart is reset to -1 so upstream
nodes stop being collected. A final reverse scan over edges returns the last edge
whose both endpoints are in cycle.

Time: O(V + E)
    Adjacency list build is O(E), DFS visits each node and edge once, final scan is O(E)
Space: O(V + E)
    Adjacency list holds O(V + E) entries; visited, cycle, and the DFS call stack each hold at most O(V)
'''
# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         # in a fully connected tree, num vertices = num edges - 1
#         # in a fully connected tree + 1 edge, num vertices = num edges
#         numVertices = len(edges)
#         # 1 indexed vertices
#         adjencyList = [[] for _ in range(numVertices + 1)]
#         visited = set()

#         for u, v in edges:
#             adjencyList[u].append(v)
#             adjencyList[v].append(u)
        
#         visited = set()
#         cycle = set()
#         cycleStart = -1

#         # return if cycle is detected
#         def dfs(node, parent):
#             nonlocal cycleStart

#             if node in visited:
#                 cycleStart = node
#                 return True

#             visited.add(node)

#             for neighbor in adjencyList[node]:
#                 # avoid fake cycle detection
#                 if neighbor == parent:
#                     continue
#                 if dfs(neighbor, node):
#                     if cycleStart != -1:
#                         cycle.add(node)
                    
#                     # during backtracking if we find cycleStart again,
#                     # stop backtracking
#                     if node == cycleStart:
#                         cycleStart = -1
#                     return True
            
#             return False
        
#         # find all cycle nodes
#         dfs(1, -1)

#         for u, v in reversed(edges):
#             if u in cycle and v in cycle:
#                 return [u, v]
        
#         return []
'''
Prims optimized solution. While we don't get n - 1 edges connected, find closest node,
keep on calculating smallest distances to nodes from currently added node to MST and add
curr to neighbor weight to total.

Time: O(N^2)
Space: O(N)
'''
class Solution:
    def manhattanDistance(self, p1, p2, points):
        return abs(points[p1][0] - points[p2][0]) + abs(points[p1][1] - points[p2][1])
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        mst_cost = 0
        edges_used = 0

        mst_nodes = set()

        # updated at every node addition
        # distance of curr min edge node being added to all other nodes
        min_distance = [math.inf] * n
        # start from node 0 to generate MST
        min_distance[0] = 0

        while edges_used < n:
            curr_min_edge = math.inf
            curr_node = -1

            for node in range(n):
                if node not in mst_nodes and curr_min_edge > min_distance[node]:
                    curr_min_edge = min_distance[node]
                    curr_node = node
            
            # add curr_node to mst
            mst_nodes.add(curr_node)
            mst_cost += curr_min_edge
            edges_used += 1

            # update min_distances from curr_node to all nodes
            for neighbor in range(n):
                if neighbor == curr_node or neighbor in mst_nodes:
                    continue
                
                weight = self.manhattanDistance(curr_node, neighbor, points)

                if min_distance[neighbor] > weight:
                    min_distance[neighbor] = weight
        
        return mst_cost

'''
Use Kruskal's algorithm to get Minimum Spanning Tree (MST) in a weighted undirected 
graph.
1. Get edge weights, sort list by weight
2. For each edge pair, use union find to detect if a cycle forms on merging 
    two points, else union them
3. Continue step 2 till we get n-1 edges. That is your MST

Time: O(n^2 logn)
    n^2 time to get edges and weights of the graph = n*(n-1) edges too
    n^2 log(n^2) time to sort O(n^2) edges = n^2 * 2*log(n) = n^2 logn

Space: O(n^2)
    n^2 edges in all_edges arr
'''
# class Solution:
#     def manhattanDistance(self, p1, p2, points):
#         return abs(points[p1][0] - points[p2][0]) + abs(points[p1][1] - points[p2][1])

#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         n = len(points)
#         all_edges = []

#         for node1 in range(n):
#             for node2 in range(node1 + 1, n):
#                 weight = self.manhattanDistance(node1, node2, points)
#                 all_edges.append((weight, node1, node2))
        
#         # sort by weight
#         all_edges.sort()

#         uf_obj = UnionFind(n)
#         # used to track min sum of weights in MST
#         mst_cost = 0
#         # to stop at n - 1 edges
#         edges_used = 0

#         for weight, node1, node2 in all_edges:
#             if uf_obj.union(node1, node2):
#                 mst_cost += weight
#                 edges_used += 1

#                 if edges_used == n - 1:
#                     break
        
#         return mst_cost if edges_used == n - 1 else -1

# class UnionFind:
#     def __init__(self, size: int) -> None:
#         # each node is its own parent initially
#         self.parent = [i for i in range(size)]
#         # each node has 0 connected nodes hence rank is 1 (just itself)
#         self.rank = [1] * size
    
#     def union(self, node1: int, node2: int) -> bool:
#         # find the top parents of node1 and node2
#         parent1 = self.find(node1)
#         parent2 = self.find(node2)
        
#         # node1 and node2 are already connected and have the same parent
#         # cannot join, will form cycle
#         if parent1 == parent2:
#             return False
        
#         if self.rank[parent1] > self.rank[parent2]:
#             self.parent[parent2] = parent1
#             # add count of nodes being added to parent1 from parent2
#             self.rank[parent1] += self.rank[parent2]
#         else:
#             # parent2 is bigger than parent1, merge 1 into 2
#             self.parent[parent1] = parent2
#             self.rank[parent2] += self.rank[parent1]

#         return True

#     # returns top parent of a node
#     def find(self, node: int) -> int:
#         while node != self.parent[node]:
#             # if node is not it's own parent, find the top parent recursively
#             # path compression
#             self.parent[node] = self.parent[self.parent[node]]
#             node = self.parent[node]

#         # return the top parent after recursion
#         return self.parent[node]

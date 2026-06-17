"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
DFS

Time: O(V + E)
      We visit each node/vertex and traverse all neighbors/edges once
Space: O(V)
      oldToNew hashmap size
'''
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {}

        def dfs(node):
            if not node:
                return
            
            if node in oldToNew:
                return oldToNew[node]
            
            newNode = Node(node.val)
            oldToNew[node] = newNode

            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            
            return newNode
        
        return dfs(node)

'''
BFS

Time: O(V + E)
      We visit each node/vertex and traverse all neighbors/edges once
Space: O(V)
      oldToNew hashmap size
'''
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         if not node:
#             return node
        
#         q = deque()
#         self.visited[node.val] = Node(node.val)
#         q.append(node)

#         while q:
#             curr = q.popleft()

#             for neighbor in curr.neighbors:
#                 if neighbor.val not in self.visited:
#                     self.visited[neighbor.val] = Node(neighbor.val)
#                     # add next neighbor for processing
#                     q.append(neighbor)

#                 # if neighbor was not visited, we created the clone
#                 # either way, we need to add cloned neighbor reference
#                 # to curr's cloned node
#                 self.visited[curr.val].neighbors.append(self.visited[neighbor.val])
        
#         return self.visited[node.val]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Recursive DFS
        Time: O(n)
            We go to every node everytime
        Space: O(h)
            h is height of tree
            Best case (balanced tree): O(logn)
            Worst case (one sided tree): O(n)
        '''
        # def dfs(node):
        #     if not node:
        #         return 0

        #     return 1 + max(dfs(node.left), dfs(node.right))

        # return dfs(root)

        '''
        OR
        '''
        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        '''
        Iterative DFS
        Time: O(n)
            We go to every node everytime
        Space: O(h)
            h is height of tree
            Best case (balanced tree): O(logn)
            Worst case (one sided tree): O(n)

            The stack holds at most the nodes along the current DFS path 
            plus their unvisited siblings, which is bounded by height
        '''
        if not root:
            return 0
        
        stack = [(root, 1)] # (node, depth)
        res = 0

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
            
        return res

        '''
        BFS
        Time: O(n)
        Space: O(n)
            because the queue can hold an entire level at once. For a complete
            binary tree the last level has ~n/2 nodes, so O(n) is the right bound
        '''
        # if not root:
        #     return 0

        # queue = deque([root])
        # level = 0

        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     level += 1
        
        # return level
  
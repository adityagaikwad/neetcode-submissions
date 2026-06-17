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
        Time:
            Best case (balanced tree): O(logn)
            Worst case (one sided tree): O(n)
        Space:
            O(h)
            h is height of tree
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
        Space: O(n)
        '''
        # if not root:
        #     return 0
        
        # stack = [(root, 1)] # (node, depth)
        # res = 0

        # while stack:
        #     node, depth = stack.pop()

        #     if node:
        #         res = max(res, depth)
        #         stack.append((node.left, depth + 1))
        #         stack.append((node.right, depth + 1))
            
        # return res

        '''
        BFS
        Time: O(n)
        Space: O(n)
        '''
        if not root:
            return 0

        queue = deque([root])
        level = 0

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        
        return level


            
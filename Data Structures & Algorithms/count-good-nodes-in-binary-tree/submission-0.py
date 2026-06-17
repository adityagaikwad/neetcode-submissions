# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # root is always a good node
        goodNodes = 0

        def dfs(node, largestSoFar):
            nonlocal goodNodes

            if not node:
                return

            if node.val >= largestSoFar:
                goodNodes += 1
                largestSoFar = node.val
            
            dfs(node.left, largestSoFar)
            dfs(node.right, largestSoFar)
        
        dfs(root, float("-inf"))
        return goodNodes
                    

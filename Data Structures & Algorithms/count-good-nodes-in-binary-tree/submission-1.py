# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
DFS

Pass largestSoFar with every dfs call and compare with node.val

Time: O(n)
Space: O(n)
'''
class Solution:
    def dfs(self, node, largestSoFar):
        if not node:
            return

        if node.val >= largestSoFar:
            self.goodNodes += 1
            largestSoFar = node.val
        
        self.dfs(node.left, largestSoFar)
        self.dfs(node.right, largestSoFar)

    def goodNodes(self, root: TreeNode) -> int:
        self.goodNodes = 0

        # root is always a good node
        self.dfs(root, float("-inf"))
        
        return self.goodNodes
                    

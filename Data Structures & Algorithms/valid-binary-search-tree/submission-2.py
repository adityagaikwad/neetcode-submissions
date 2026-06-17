# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, leftMin, rightMax):
            if not node:
                return True
            
            if not (leftMin < node.val < rightMax):
                return False
            
            # for node.left the max val must be less than node.val
            # for node.right the min val must be greater than node.val
            return dfs(node.left, leftMin, node.val) and\
                   dfs(node.right, node.val, rightMax)
        
        return dfs(root, float("-inf"), float("inf"))
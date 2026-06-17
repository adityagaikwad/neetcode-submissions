# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
DFS with inherited min/max bounds

Every node must satisfy leftMin < node.val < rightMax.
Start with (-inf, inf) at the root, then tighten the bounds as we go:
    - going left:  node.val becomes the new rightMax (left subtree must be < node.val)
    - going right: node.val becomes the new leftMin  (right subtree must be > node.val)

This propagates all ancestor constraints down so every node is validated
against the full BST property, not just its immediate parent.

Time: O(n)
    Each node visited once
Space: O(h) = O(n)
    Call stack depth equals tree height
'''
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
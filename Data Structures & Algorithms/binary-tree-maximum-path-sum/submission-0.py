# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPathVal = float("-inf")

        def gainFromSubtree(node):
            nonlocal maxPathVal

            if not node:
                return 0
            
            # if leftMax from subtree is < 0 then we do not
            # consider the subtree in max path. Same for right subtree
            leftMax = max(gainFromSubtree(node.left), 0)
            rightMax = max(gainFromSubtree(node.right), 0)

            maxPathVal = max(maxPathVal, node.val + leftMax + rightMax)

            return max(node.val + leftMax, node.val + rightMax)

        gainFromSubtree(root)
        return maxPathVal
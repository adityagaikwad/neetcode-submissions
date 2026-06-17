# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def depth(node):
            if not node:
                return 0
            
            nonlocal diameter

            leftPathDepth = depth(node.left)
            rightPathDepth = depth(node.right)

            # since diameter is height sum
            diameter  = max(diameter, leftPathDepth + rightPathDepth)

            # return depth from root node
            return 1 + max(leftPathDepth, rightPathDepth)
        
        depth(root)

        return diameter
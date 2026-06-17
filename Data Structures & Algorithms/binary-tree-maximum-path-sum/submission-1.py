# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Recursive DFS with global max tracker

gainFromSubtree returns the best single-branch gain reachable from a node upward
to its parent: the node's value plus whichever child contributes more. It cannot
return both branches combined because the parent would receive a forked path, which
violates the path definition. As a side effect, it updates maxPathVal with the best
path that peaks at the current node, which may span both children since the path
terminates there and does not continue upward.

Clamping leftMax and rightMax to 0 handles negative subtrees: a negative branch
only reduces the total, so we treat it as contributing nothing and exclude it.

Time: O(n)
    Each node visited once
Space: O(h)
    Call stack depth equals tree height
    O(log n) balanced / O(n) skewed
'''
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
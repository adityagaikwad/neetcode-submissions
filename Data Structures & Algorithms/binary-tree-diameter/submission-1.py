# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxDiameter = 0

    def depth(self, root: Optional[TreeNode]) -> int:
        '''
        Returns the number of nodes on the longest path from root downward,
        and as a side effect tracks the longest diameter seen through any node.

        Why diameter at a node = leftDepth + rightDepth (no +1):
            depth(root.left) returns edges from root.left to its deepest leaf + 1.
            But that +1 exactly accounts for the edge between root and root.left,
            so leftDepth is already the number of edges from root going left.
            Same for rightDepth. The diameter through this node is the total
            edges on the path (deepest left) -> root -> (deepest right),
            which is just leftDepth + rightDepth.

        Time:  O(n)  -- each node visited once
        Space: O(h)  -- call stack depth equals tree height
        '''
        if not root:
            return 0

        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)

        # path through this node spans leftDepth edges left + rightDepth edges right
        self.maxDiameter = max(self.maxDiameter, leftDepth + rightDepth)

        # reuse cached values -- calling self.depth again here would make it O(n^2)
        return 1 + max(leftDepth, rightDepth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.depth(root)

        return self.maxDiameter
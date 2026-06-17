# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    Brute force

    Time: O(n log n)
        Each isBalanced call calls depth for O(N)
        + if time for first N is T(N) then left and right
        will be 2T(N/2)
        T(N) = 2T(N/2)+O(N)
             = 2(2T(N/4)+O(N/2))+O(N)
             = 4T(N/4)+O(N)+O(N)
             ... O(N log N)
    Space: O(n) skewed tree
    '''
    # def depth(self, node):
    #         if not node:
    #             return 0

    #         return 1 + max(
    #             self.depth(node.left),
    #             self.depth(node.right)
    #         )

    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True
        
    #     leftDepth = self.depth(root.left)
    #     rightDepth = self.depth(root.right)

    #     return abs(leftDepth - rightDepth) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)
    '''
    DFS

    Time: O(n)
    Space: O(n)
    '''
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # calculate depth and check if subtree is balanced in same call
        def dfs(node):
            if not node:
                # isBalanced, depth
                return [True, 0]
            
            # calculate isBalanced and depth of left and right
            # subtrees recursively
            left, right = dfs(node.left), dfs(node.right)

            balancedTree = left[0] and right[0] and abs(left[1] - right[1]) < 2

            return [balancedTree, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]
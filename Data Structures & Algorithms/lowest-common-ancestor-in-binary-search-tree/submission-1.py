# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        Recursion
        O(h) for both
        '''
        # if not root or not p or not q:
        #     return None

        # if max(p.val, q.val) < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # elif min(p.val, q.val) > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # else:
        #     return root
        
        '''
        Iterative
        Time: O(h)
        Space: O(1)
        '''
        if not root or not p or not q:
            return None
        
        curr = root

        while curr:
            # search left subtree for LCA
            if max(p.val, q.val) < curr.val:
                curr = curr.left
            # search right subtree for LCA
            elif min(p.val, q.val) > curr.val:
                curr = curr.right
            else:
                return curr
        
        return None

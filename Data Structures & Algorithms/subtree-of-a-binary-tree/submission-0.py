# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        Time: O(N * M)
            N is nodes in root
            M is nodes in subroot
            Since for every node in N, we compare with all M nodes
        Space: O(N + M)
            
        '''
        def dfs(node):
            if not node:
                return False

            if isSameTree(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)

        def isSameTree(node1, node2):
            if not node1 and not node2:
                return True
            
            # only one is None
            if not node1 or not node2:
                return False

            return node1.val == node2.val and\
                isSameTree(node1.left, node2.left) and\
                isSameTree(node1.right, node2.right)
        
        return dfs(root)
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
        # def dfs(node):
        #     if not node:
        #         return False

        #     if isSameTree(node, subRoot):
        #         return True
            
        #     return dfs(node.left) or dfs(node.right)

        # def isSameTree(node1, node2):
        #     if not node1 and not node2:
        #         return True
            
        #     # only one is None
        #     if not node1 or not node2:
        #         return False

        #     return node1.val == node2.val and\
        #         isSameTree(node1.left, node2.left) and\
        #         isSameTree(node1.right, node2.right)
        
        # return dfs(root)

        '''
        Serialization of tree + substring match
        Serialize with preorder - "^+val+left+right"
        Note: Add ^ and then val
              For null, add "#"
        Time: O(N * M)
        Space: O(N + M)
        '''
        r = self.serialize(root)
        s = self.serialize(subRoot)

        # O(n*m) worst case
        return s in r
        
        # O(n + m) will be using KMP

    def serialize(self, node):
        if node == None:
            return "#"

        return "^" + str(node.val) + self.serialize(node.left) + self.serialize(node.right)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Time: O(N * M)
    N is nodes in root
    M is nodes in subroot
    Since for every node in N, we compare with all M nodes
Space: O(N + M)  
'''
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if both don't exist, valid
        if not root and not subRoot:
            return True

        # if either doesn't exist or vals don't match, invalid
        if not root or not subRoot or root.val != subRoot.val:
            return False
        
        return (
            self.sameTree(root.left, subRoot.left) and
            self.sameTree(root.right, subRoot.right)
        )
        
        return False

'''
Serialization of tree + substring match
Serialize with preorder - "^+val+left+right"
Note: Add ^ and then val
        For null, add "#"
Time: O(N * M)
Space: O(N + M)
'''
# class Solution:   
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         r = self.serialize(root)
#         s = self.serialize(subRoot)

#         # O(n*m) worst case
#         return s in r
        
#         # O(n + m) will be using KMP

#     def serialize(self, node):
#         if node == None:
#             return "#"

#         return "^" + str(node.val) + self.serialize(node.left) + self.serialize(node.right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    Time: O(n) worst case
        O(logn) best case (balanced tree)
    Space: O(n)
    '''
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (p and not q):
            return False

        if not p and not q:
            return True
        
        isLeftEqual = self.isSameTree(p.left, q.left)

        isRightEqual = self.isSameTree(p.right, q.right)

        return p.val == q.val and isLeftEqual and isRightEqual
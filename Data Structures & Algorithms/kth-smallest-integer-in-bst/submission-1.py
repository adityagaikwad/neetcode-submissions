# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        Recursive inorder
        O(n) Time and Space
        
        inorder traversal of BST returns sorted arr
        return arr[k - 1] O(n)
        but goes to all nodes
        instead we can count k at inorder traversal and return kth node
        '''
        # res = root.val
        # count = k
        # def inorder(node):
        #     nonlocal count, res

        #     if not node:
        #         return

        #     inorder(node.left)
        #     # in inorder traversal, when we visit node
        #     # it is always sorted. So when we get to kth node
        #     # that is our kth smallest node
        #     count -= 1
        #     if count == 0:
        #         res = node.val
        #         return

        #     inorder(node.right)
        
        # inorder(root)
        # return res

        '''
        Iterative inorder

        O(n) Time and Space
        '''
        stack = []
        curr = root

        while stack or root:
            while curr:
                # add elements to stack in LVR order
                stack.append(curr)
                curr = curr.left
            
            # Visit after all left nodes are added
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

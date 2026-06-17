# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        DFS 1
        Time: O(n^2)
        Space: O(n)
        '''
        # def dfs(inorder, preorder):
        #     if not preorder or not inorder:
        #         return None

        #     rootVal = preorder[0]
        #     root = TreeNode(rootVal)
        #     rootPos = inorder.index(preorder[0])
        #     # left subtree is inorder[:rootPos],
        #     #   preorder[1:rootPos] coz num elements in left subtree = rootPos - 1
        #     # right subtree is inorder[rootPos + 1:]
        #     #   preorder[rootPos+ 1:] coz num elements in right subtree = rootPos + 1 to end
        #     root.left = dfs(inorder[:rootPos], preorder[1: rootPos + 1])
        #     root.right = dfs(inorder[rootPos + 1:], preorder[rootPos + 1:])

        #     return root

        # return dfs(inorder, preorder)

        '''
        Recursive optimized with hashmap
        Time: O(n)
        Space: O(n)
        '''
        if not preorder or not inorder:
            return None

        inOrderIndexes = {val: i for i, val in enumerate(inorder)}
        preOrderPos = 0

        def dfs(left, right):
            # left and right are inclusive here
            nonlocal preOrderPos

            if left > right:
                return None
            
            # get the next node to add
            rootVal = preorder[preOrderPos]
            # get the location of node in inorder
            inOrderPos = inOrderIndexes[rootVal]
            
            root = TreeNode(rootVal)
            preOrderPos += 1

            # left subtree = left to inorderPos - 1
            # right subtree = inorderPos + 1 to right
            root.left = dfs(left, inOrderPos - 1)
            root.right = dfs(inOrderPos + 1, right)

            return root
        
        return dfs(0, len(inorder) - 1)

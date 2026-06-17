# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
DFS 1
Time: O(n^2)
Space: O(n)
'''
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         def dfs(inorder, preorder):
#             if not preorder or not inorder:
#                 return None

#             rootVal = preorder[0]
#             root = TreeNode(rootVal)
#             rootPos = inorder.index(preorder[0])
#             # left subtree is inorder[:rootPos],
#             #   preorder[1:rootPos + 1] (+1 is exclusive)
#             #   coz we have do rootPos - 1 in left subtree and also next
#             #   rootPos - 1 nodes in preorder are all left subtree
#             # right subtree is inorder[rootPos + 1:]
#             #   preorder[rootPos+ 1:] coz num elements in right subtree = rootPos + 1 to end
#             root.left = dfs(inorder[:rootPos], preorder[1: rootPos + 1])
#             root.right = dfs(inorder[rootPos + 1:], preorder[rootPos + 1:])

#             return root

#         return dfs(inorder, preorder)

'''
Recursive optimized with hashmap. Store idxs of inorder in hashmap first.
Keep global preOrderPos, then, do dfs(l, r) and ger curr root from
preorder[preOrderPos]. We have inOrderPos too from hashmap, then set curr as root
and recursively do
root.left = dfs(left, inOrderPos - 1) (has inorderPos - 1 nodes on left)
root.right = dfs(inOrderPos + 1, right)

Time: O(n)
Space: O(n)
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
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

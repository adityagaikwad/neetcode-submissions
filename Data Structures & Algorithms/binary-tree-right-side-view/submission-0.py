# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node, depth):
            if not node:
                return
            
            # i.e the curr node is the first node at
            # treeDepth = depth + 1
            # it's like marking visited at depth = depth + 1
            if len(ans) == depth:
                ans.append(node.val)
            
            # go as right as possible if right is none, go left and then
            # recursion will make it go right again first
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return ans

        '''
        Another approach is BFS
        Do level order traversal and add the rightmost node
        at each level to ans
        '''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
DFS approach

Use depth parameter to track which level each node belongs to.
When we first visit a new level (len(res) == depth), append a new sublist.
Then append the current node's value to res[depth].

Since DFS visits left before right, nodes within each level are added
left to right automatically - no extra ordering needed.

Time: O(n)
Space: O(n)
'''
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res = []

#         def dfs(node, depth):
#             if not node:
#                 return None
#             if len(res) == depth:
#                 res.append([])

#             res[depth].append(node.val)
#             dfs(node.left, depth + 1)
#             dfs(node.right, depth + 1)

#         dfs(root, 0)
#         return res

'''
BFS approach

Exhaust all nodes in curr queue (only nodes of curr level are in queue at a time)
Then add all left and right nodes for each popleft node to queue to process later

Ensure to calculate len of queue before you start popping to avoid popping nodes from
curr level nodes' children

Keep an arr levelNodes for adding each level's node vals which you add to res
at the end of the curr level traversal

Time: O(n)
Space: O(n)
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])

        while queue:
            queueLen = len(queue)
            levelNodes = []
            for i in range(queueLen):
                node = queue.popleft()
                levelNodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if levelNodes:
                ans.append(levelNodes)

        return ans
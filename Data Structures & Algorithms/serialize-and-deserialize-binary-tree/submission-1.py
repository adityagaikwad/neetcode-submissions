# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    '''
    Level order traversal
    O(n) time and space
    '''
    # # Encodes a tree to a single string.
    # def serialize(self, root: Optional[TreeNode]) -> str:
    #     # use level order traversal
    #     if not root:
    #         return "N"
        
    #     queue = deque([root])
    #     res = []
    #     while queue:
    #         levelNodes = []
    #         n = len(queue)
    #         for i in range(n):
    #             node = queue.popleft()
    #             if node:
    #                 res.append(str(node.val))
    #                 queue.append(node.left)
    #                 queue.append(node.right)
    #             else:
    #                 res.append("N")

    #     return ",".join(res)

    # # Decodes your encoded data to tree.
    # def deserialize(self, data: str) -> Optional[TreeNode]:
    #     nodes = data.split(",")
    #     if nodes[0] == "N":
    #         return None

    #     root = TreeNode(int(nodes[0]))
    #     queue = deque([root])
    #     nextNode = 1

    #     while queue:
    #         node = queue.popleft()

    #         if nodes[nextNode] != "N":
    #             node.left = TreeNode(int(nodes[nextNode]))            
    #             queue.append(node.left)
    #         nextNode += 1

    #         if nodes[nextNode] != "N":
    #             node.right = TreeNode(int(nodes[nextNode]))
    #             queue.append(node.right)
    #         nextNode += 1

    #     return root
    '''
    DFS preorder traversal
    O(n) time and space
    '''
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)        
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")

        nextNode = 0
        def dfs():
            nonlocal nextNode

            nodeVal = nodes[nextNode]
            nextNode += 1
            if nodeVal == "N":
                return None

            root = TreeNode(int(nodeVal))
            root.left = dfs()
            root.right = dfs()

            return root
        
        return dfs()
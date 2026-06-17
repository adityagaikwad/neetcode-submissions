class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

    def add(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]

        curr.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Node()
        for word in words:
            root.add(word)
        
        nRows = len(board)
        nCols = len(board[0])
        res = set()
        visited = set()

        def dfs(r, c, currNode, currWord):
            if (r < 0 or r >= nRows or
                c < 0 or c >= nCols or
                (r, c) in visited or
                board[r][c] not in currNode.children
            ):
                return

            visited.add((r, c))
            currNode = currNode.children[board[r][c]]
            currWord += board[r][c]

            if currNode.isEnd:
                res.add(currWord)
            
            dfs(r + 1, c, currNode, currWord)
            dfs(r - 1, c, currNode, currWord)
            dfs(r, c + 1, currNode, currWord)
            dfs(r, c - 1, currNode, currWord)

            # backtrack to explore other options
            visited.remove((r, c))
        
        for r in range(nRows):
            for c in range(nCols):
                dfs(r, c, root, "")
        
        return list(res)
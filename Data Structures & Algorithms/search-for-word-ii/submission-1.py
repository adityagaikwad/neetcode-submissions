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
        '''
        Add words to trie to allow early rejection in case word's next char is not in trie
        Instead of checking for all words at all traversal steps.
        Time Complexity: O(M * (4* 3 ^ (L - 1)))
            M cells, we do DFS from each cell. Worst case we first explore all 4 directions.
            Then for each of those there's 3 unexlored directions (since we came from one)
            So 3 ^ L-1 since 1 char is covered in first 4 direction char check.
            
            M is total cells, r * c
            L is max len of any word in the array

        One optimization could be to remove a matched word from trie to avoid exploring that 
        DFS again for similar words in wordList.

        Space: O(N) where N is total letters across the words list
            When there is no overlap between the word prefixes for trie nodes.
        '''
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
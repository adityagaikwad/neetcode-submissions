'''
Time: O(r x c x 4^k)
    4^k comes from exploring 4 directions recursively for each
    letter in the word of length k
    We start search from each cell of the board so r x c x 4^k

OR O(r x c x 3^k)
initially we could have at most 4 directions to explore,
but further the choices are reduced into 3,
since we won't go back to where we come from

Space: O(k) for the recursion when word is found
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nRow = len(board)
        nCol = len(board[0])
        wordLen = len(word)

        def backtrack(currWordPtr, row, col):
            if currWordPtr == wordLen:
                return True

            if (row < 0 or row >= nRow
             or col < 0 or col >= nCol
             or board[row][col] != word[currWordPtr]):
                return False
            
            prevBoardVal = board[row][col]
            # use board to mark as visited
            board[row][col] = "#"

            res = (backtrack(currWordPtr + 1, row + 1, col) or 
                    backtrack(currWordPtr + 1, row - 1, col) or 
                    backtrack(currWordPtr + 1, row, col + 1) or 
                    backtrack(currWordPtr + 1, row, col - 1))
            
            # restore visited on board
            board[row][col] = prevBoardVal

            return res

        for i in range(nRow):
            for j in range(nCol):
                if board[i][j] == word[0] and backtrack(0, i, j):
                    return True
        
        return False

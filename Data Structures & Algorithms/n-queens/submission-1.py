'''
backtrack(board, row, visitedC, visitedNegDiag, visitedPosDiag)
Try adding a valid queen on each row by iterating to each col on that row
and checking if this row,col is not marked visited on col, posDiag and negDiag

backtracking one row at a time ensures max 1 queen per row

Time: O(N!)
      First row has N col options, second has N - 1 and so on

Space: O(N^2)
       board takes N^2 space, sets take O(N) space
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:        
        res = []
        
        def generate_board(board):
            s = []
            for row in board:
                s.append("".join(row))
            return s

        def backtrack(board, row, visitedC, visitedNegDiag, visitedPosDiag):
            # meaning queens have been successfully placed on 0 - (n-1) rows
            # board is complete
            if row == n:
                res.append(generate_board(board))
                return
            
            for col in range(n):
                # top left to bottom right downward diagonals
                # we increase one in row and col per entry in these diags
                # so row - col is constant
                negDiag = row - col
                # bottom left to top right upwards diagonals
                # we decrease in row and increase in col
                # so row + col stays constant
                posDiag = row + col

                # If the queen is not placeable, continue to next col
                if (
                    col in visitedC or
                    negDiag in visitedNegDiag or
                    posDiag in visitedPosDiag
                ):
                    continue
                
                # add queen since its a valid pos and try backtracking remaining rows
                board[row][col] = "Q"
                visitedC.add(col)
                visitedNegDiag.add(negDiag)
                visitedPosDiag.add(posDiag)

                # Move on to the next row with the updated board state
                backtrack(board, row + 1, visitedC, visitedNegDiag, visitedPosDiag)
                
                # reset queen to try another col on the same row
                board[row][col] = "."
                visitedC.remove(col)
                visitedNegDiag.remove(negDiag)
                visitedPosDiag.remove(posDiag)
        
        '''
        NOTE: Do not do list multiplication for empty board input!!
        This creates a shallow copy, meaning all rows in empty_board point
        to the same list in memory.
        empty_board = [["."] * n] * n
        '''
        board = [["."] * n for _ in range(n)]
        
        backtrack(board, 0, set(), set(), set())

        return res

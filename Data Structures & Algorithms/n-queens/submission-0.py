class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:        
        board = [["."] * n for _ in range(n)]
        res = []
        
        def generate_board(board):
            s = []
            for row in board:
                s.append("".join(row))
            return s

        def backtrack(board, row, visitedC, visitedD, visitedAD):
            if row == n:
                res.append(generate_board(board))
                return
            
            for col in range(n):
                currDiag = row - col
                antiDiag = row + col

                if (
                    col in visitedC or
                    currDiag in visitedD or
                    antiDiag in visitedAD
                ):
                    continue
                
                board[row][col] = "Q"
                visitedC.add(col)
                visitedD.add(currDiag)
                visitedAD.add(antiDiag)

                backtrack(board, row + 1, visitedC, visitedD, visitedAD)
                
                board[row][col] = "."
                visitedC.remove(col)
                visitedD.remove(currDiag)
                visitedAD.remove(antiDiag)
        
        backtrack(board, 0, set(), set(), set())

        return res

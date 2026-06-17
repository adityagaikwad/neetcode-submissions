from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        boxSet = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                box = (row // 3, col // 3)

                if (
                    board[row][col] in rowSet[row]
                    or board[row][col] in colSet[col]
                    or board[row][col] in boxSet[box]
                ):
                    return False

                rowSet[row].add(board[row][col])
                colSet[col].add(board[row][col])
                boxSet[box].add(board[row][col])
        
        return True

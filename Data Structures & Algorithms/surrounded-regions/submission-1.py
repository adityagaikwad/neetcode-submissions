'''
Border Os and their connected islands cannot be captured

DFS from 4 borders' Os and mark the connected Os as Ts

Then iterate board, turn all remaining Os to Xs
If its not a O but a T then turn it back to O (IMP to check if its O first)

This way we marked all islands with Os at border, then mark non border island Os
as Xs as they are captured and then return the other ones back to O from T

Time: O(r x c)

Space: O(1)
    In place change
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        # mark O's as visited function
        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or 
                c == COLS or board[r][c] != "O"
            ):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # mark regions starting at left and right border as T
        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)
        
        # mark regions starting at top and bottom border as T
        for c in range(COLS):
            if board[0][c] == "O":
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)

        # flip and return
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

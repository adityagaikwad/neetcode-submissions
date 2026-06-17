class Solution:
    '''
    3 pass 3 hashsets solution

    Time: O(n^2)
    Space: O(n)
    '''
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     for row in range(9):
    #         seen = set()
    #         for col in range(9):
    #             if board[row][col] == ".":
    #                 continue
                
    #             if board[row][col] in seen:
    #                 return False
                
    #             seen.add(board[row][col])
        
    #     for col in range(9):
    #         seen = set()
    #         for row in range(9):
    #             if board[row][col] == ".":
    #                 continue
                
    #             if board[row][col] in seen:
    #                 return False
                
    #             seen.add(board[row][col])

    #     for square in range(9):
    #         seen = set()
    #         for i in range(3):
    #             for j in range(3):
    #                 row = (square // 3)*3 + i
    #                 col = (square % 3)*3 + j

    #                 if board[row][col] == ".":
    #                     continue
                
    #                 if board[row][col] in seen:
    #                     return False
                    
    #                 seen.add(board[row][col])
        
    #     return True

    '''
    One pass 3 hashsets
    rows = defaultdict(set)
        rows[r] has entries for seen digits in that row
    same with cols defaultdict

    squares = defaultdict(set) with key = tuple((r // 3, c // 3))
        we get 9 unique tuples depicting the 9 squares this way
        we store the 9 digits seen in this square in squares[tuple] set

    While iterating from each cell, we check all 3 seen, whenever we see
    a repeat in any sets, we return false

    Time: O(n^2)
    Space: O(n^2)
        The hash sets rows, cols, and squares collectively store at most 
        n^2 entries across all keys, one per non-empty cell
    '''
    from collections import defaultdict

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                
                if (
                    board[row][col] in rows[row]
                    or board[row][col] in cols[col]
                    or board[row][col] in squares[(row//3, col//3)]
                ):
                    return False

                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row//3, col//3)].add(board[row][col])
        
        return True

    '''
    Bitmask solution, use rows = [0] * 9 each row's num being the bitmask
    for that row. if a row has 3,5 the bitmask would be 000 010 100 coz
    the 1's represent this - 987 654 321
    
    rows[r] = 000010100 means the row already has digits 3 and 5.
    mask = 000010000 means we are checking whether digit 5 exists.
    rows[r] & mask != 0, so the 5 bit matches → duplicate 5 found.
    & operation should be zero if there is no overlap.

    rows[r] |= mask adds the digit to the row as seen

    Time: O(n^2)
    Space: O(n)
    '''
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     rows = [0] * 9
    #     cols = [0] * 9
    #     squares = [0] * 9

    #     for r in range(9):
    #         for c in range(9):
    #             if board[r][c] == ".":
    #                 continue

    #             val = int(board[r][c]) - 1
    #             if (1 << val) & rows[r]:
    #                 return False
    #             if (1 << val) & cols[c]:
    #                 return False
    #             if (1 << val) & squares[(r // 3) * 3 + (c // 3)]:
    #                 return False

    #             rows[r] |= (1 << val)
    #             cols[c] |= (1 << val)
    #             squares[(r // 3) * 3 + (c // 3)] |= (1 << val)

    #     return True

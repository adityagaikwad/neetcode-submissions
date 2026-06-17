class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        O(n) time and space solution
        '''
        ROWS, COLS = len(matrix), len(matrix[0])
        rows, cols = [False] * ROWS, [False] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True

        for r in range(ROWS):
            for c in range(COLS):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0
        
        '''
        Time: O(n)
        Space: O(1)
        
        We use the first row and first column of the matrix as markers to
        track which rows and columns need to be zeroed, avoiding extra space.
        
        While traversing the matrix, whenever we find a 0, we mark its row and
        column by setting matrix[r][0] and matrix[0][c] to 0
        
        Since matrix[0][0] overlaps as both row and column marker,
        we use an extra variable rowZero to track if the first row needs to be zeroed
        
        After marking, we iterate the matrix (excluding first row and column) and set matrix[r][c] = 0 if 
        its row or column is marked. Finally, we handle the first column separately
        using matrix[0][0], and the first row using rowZero. This way,
        the matrix is updated in-place with O(1) space.
        '''
        
        # ROWS, COLS = len(matrix), len(matrix[0])
        # rowZero = False

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if matrix[r][c] == 0:
        #             matrix[0][c] = 0
        #             if r > 0:
        #                 matrix[r][0] = 0
        #             else:
        #                 rowZero = True

        # for r in range(1, ROWS):
        #     for c in range(1, COLS):
        #         if matrix[0][c] == 0 or matrix[r][0] == 0:
        #             matrix[r][c] = 0

        # if matrix[0][0] == 0:
        #     for r in range(ROWS):
        #         matrix[r][0] = 0

        # if rowZero:
        #     for c in range(COLS):
        #         matrix[0][c] = 0
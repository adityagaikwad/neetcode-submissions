class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        Two pass binary search

        Time complexity:
            O(logm+logn)
            which reduces to O(log(m x n))
        Space complexity:
            O(1)
        '''
        # startRow = 0
        # endRow = len(matrix) - 1

        # while startRow <= endRow:
        #     midRow = startRow + (endRow - startRow)//2

        #     # if target is bigger than the largest value of midRow
        #     # go to higher row to find target
        #     if target > matrix[midRow][-1]:
        #         startRow = midRow + 1
        #     # if target is smaller than smalles value in midRow
        #     # go to lower row to find target
        #     elif target < matrix[midRow][0]:
        #         endRow = midRow - 1
        #     else:
        #         finalRow = midRow
        #         break

        # if startRow > endRow:
        #     return False

        # startCol = 0
        # endCol = len(matrix[0]) - 1

        # while startCol <= endCol:
        #     midCol = startCol + (endCol - startCol)//2

        #     if matrix[finalRow][midCol] < target:
        #         startCol = midCol + 1
        #     elif matrix[finalRow][midCol] > target:
        #         endCol = midCol - 1
        #     else:
        #         return True
        
        # return False

        '''
        One pass binary search
        
        Time complexity:
            O(logm+logn)
            which reduces to O(log(m x n))
        Space complexity:
            O(1)
        '''
        m = len(matrix)
        if m == 0:
            return False

        n = len(matrix[0])

        # binary search
        # We can consider the matrix as one straight 1D arr
        # start with 0 to n cols with row 0
        # then 0 to n with row 1 and so on
        # i.e first n are matrix[0][1-n] i.e 
        # (0 + m*n - 1) // n and % n for row and col
        left, right = 0, m * n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False
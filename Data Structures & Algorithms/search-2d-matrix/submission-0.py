class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        startRow = 0
        endRow = len(matrix) - 1

        while startRow <= endRow:
            midRow = startRow + (endRow - startRow)//2

            if matrix[midRow][0] <= target <= matrix[midRow][-1]:
                startRow = midRow
                break
            elif matrix[midRow][0] < target:
                startRow = midRow + 1
            else:
                #  matrix[midRow][0] > target
                endRow = midRow - 1

        if startRow > endRow:
            return False

        # startRow is idx of the final row in which target exists
        print(startRow)

        startCol = 0
        endCol = len(matrix[0])

        while startCol <= endCol:
            midCol = startCol + (endCol - startCol)//2

            if matrix[startRow][midCol] < target:
                startCol = midCol + 1
            elif matrix[startRow][midCol] > target:
                endCol = midCol - 1
            else:
                return True
        
        return False
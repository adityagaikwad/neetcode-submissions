class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        startRow = 0
        endRow = len(matrix) - 1

        while startRow <= endRow:
            midRow = startRow + (endRow - startRow)//2

            # if target is bigger than the largest value of midRow
            # go to higher row to find target
            if target > matrix[midRow][-1]:
                startRow = midRow + 1
            # if target is smaller than smalles value in midRow
            # go to lower row to find target
            elif target < matrix[midRow][0]:
                endRow = midRow - 1
            else:
                finalRow = midRow
                break

        if startRow > endRow:
            return False

        startCol = 0
        endCol = len(matrix[0]) - 1

        while startCol <= endCol:
            midCol = startCol + (endCol - startCol)//2

            if matrix[finalRow][midCol] < target:
                startCol = midCol + 1
            elif matrix[finalRow][midCol] > target:
                endCol = midCol - 1
            else:
                return True
        
        return False
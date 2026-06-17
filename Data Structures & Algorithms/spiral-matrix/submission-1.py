class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        Time: O(m * n)
        Space: O(1)

        We use four boundaries to keep track of the current layer of the matrix:
            top: the first row that hasn't been traversed yet
            bottom: the last row that hasn't been traversed yet
            left: the first column not yet traversed
            right: the last column not yet traversed

        We loop and move in 4 directions:
            Left → Right (top row)
            Top → Bottom (right column)
            Right → Left (bottom row)
            Bottom → Top (left column)

        After each direction, we shrink the boundary inward.
        '''
        res = []
        if not matrix:
            return res

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. Traverse from left to right on the top row
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # 2. Traverse from top to bottom on the right column
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # 3. Traverse from right to left on the bottom row
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            # 4. Traverse from bottom to top on the left column
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res
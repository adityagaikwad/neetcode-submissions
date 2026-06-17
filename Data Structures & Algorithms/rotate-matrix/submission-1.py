class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            # total number of rotations are n - 1 for first row
            # then n - 3 and so on
            for i in range(r - l):
                top, bottom = l, r

                # save the topleft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1
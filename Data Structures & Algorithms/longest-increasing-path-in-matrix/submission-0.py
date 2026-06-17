class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        nRows = len(matrix)
        nCols = len(matrix[0])
        
        memo = {}
        def dfs(row, col, prevVal):
            if (
                row < 0 or row >= nRows or
                col < 0 or col >= nCols or
                matrix[row][col] <= prevVal
            ):
                # only explore if increasing path
                return 0
            
            if (row, col) in memo:
                return memo[(row, col)]

            # include curr element in longest sequence so 1 + dfs()            
            res = 1
            res = max(res, 1 + dfs(row + 1, col, matrix[row][col]))
            res = max(res, 1 + dfs(row - 1, col, matrix[row][col]))
            res = max(res, 1 + dfs(row, col + 1, matrix[row][col]))
            res = max(res, 1 + dfs(row, col - 1, matrix[row][col]))

            memo[(row, col)] = res

            return memo[(row, col)]
        
        res = -1
        for r in range(nRows):
            for c in range(nCols):
                res = max(res, dfs(r, c, -1))
        
        return res
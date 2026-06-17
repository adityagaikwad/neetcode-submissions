class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        nRows = len(grid)
        nCols = len(grid[0])

        neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col):
            if row < 0 or row >= nRows or col < 0 or col >= nCols or grid[row][col] == "0":
                return

            grid[row][col] = "0"

            for x, y in neighbors:
                dfs(row + x, col + y)
        
        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        
        return islands
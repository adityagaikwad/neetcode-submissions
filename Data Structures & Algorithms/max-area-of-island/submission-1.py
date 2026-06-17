class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        nRows = len(grid)
        nCols = len(grid[0])

        neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col, currArea):
            if row < 0 or row >= nRows or col < 0 or col >= nCols or grid[row][col] == 0:
                return 0

            # mark visited
            grid[row][col] = 0

            # include current box in area
            currArea = 1

            for x, y in neighbors:
                currArea += dfs(row + x, col + y, currArea)
            
            return currArea
        
        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == 1:
                    islandArea = dfs(i, j, 0)
                    maxArea = max(maxArea, islandArea)
        
        return maxArea
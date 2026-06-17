'''
Time: O(r * c)
    Each cell is visited once
Space: O(r * c)
    Worst case stack can go to r * c depth when whole grid is one island
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nRows = len(grid)
        nCols = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= nRows or c < 0 or c >= nCols or grid[r][c] == "0":
                return
            
            # mark visited
            grid[r][c] = "0"
            neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for x, y in neighbors:
                dfs(r + x, c + y)

        islands = 0
        for r in range(nRows):
            for c in range(nCols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        return islands
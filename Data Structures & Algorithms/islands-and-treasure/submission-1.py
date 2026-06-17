class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        Time: O(r x c)
            Since we go over each cell max once
        Space: O(r x c)
            Since queue may hold all cells in the worst case
        '''
        INF = 2**31 - 1
        nRows = len(grid)
        nCols = len(grid[0])

        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        queue = deque()

        # add all treasure chests to queue
        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        
        # BFS from all 0s
        while queue:
            row, col, dist = queue.popleft()

            for x, y in neighbors:
                newRow, newCol = row + x, col + y

                # If it's a valid land cell and not visited yet
                # Since when we visit first time from treasure will
                # be it's shortest distance
                if (
                    (0 <= newRow < nRows) and
                    (0 <= newCol < nCols) and
                    grid[newRow][newCol] == INF
                ):
                    grid[newRow][newCol] = dist + 1
                    # Add to queue for further exploration
                    queue.append((newRow, newCol, dist + 1))
                    




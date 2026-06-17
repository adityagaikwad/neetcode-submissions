class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        O(n x m) Time and Space
        '''
        totalTime = -1
        freshOranges = 0
        queue = deque()

        max_row = len(grid)
        max_col = len(grid[0])

        for i in range(max_row):
            for j in range(max_col):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        # delimiter for each round
        queue.append((-1, -1))

        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            next_i, next_j = queue.popleft()

            if next_i == -1:
                totalTime += 1

                if queue:
                    # start new round if there are still rotten oranges
                    queue.append((-1, -1))
            else:
                # process rotten orange
                for i, j in neighbors:
                    n_i, n_j = next_i + i, next_j + j

                    if max_row > n_i >= 0 and max_col > n_j >= 0:
                        if grid[n_i][n_j] == 1:
                            grid[n_i][n_j] = 2
                            queue.append((n_i, n_j))
                            freshOranges -= 1
        
        return totalTime if freshOranges == 0 else -1

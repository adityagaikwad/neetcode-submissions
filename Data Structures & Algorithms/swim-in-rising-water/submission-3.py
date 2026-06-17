class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        Djikstra's algo, i.e Min heap approach -
        1. Add smallest num from 4 directions to queue.
        2. Keep visiting smallest till we reach bottom right.
            total time = max of the smallest elevations we encounter 
            since at max time we can swim across this path in one go

        Time Complexity: O(N^2logN)
            We may expand O(N^2) nodes, and each one
            requires O(logN) time to perform the heap operations

        Space Complexity: O(N^2)
            The maximum size of the heap
        '''
        N = len(grid)

        visited = set()
        # (height, row, col)
        minHeap = [(grid[0][0], 0, 0)]
        maxHeight = 0
        
        while minHeap:
            height, r, c = heapq.heappop(minHeap)
            visited.add((r, c))
            
            # max height encountered is total time taken
            # since at max time we can swim across this path in one go
            maxHeight = max(maxHeight, height)

            if r == c == N - 1:
                return maxHeight

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if (
                    0 <= nr < N and
                    0 <= nc < N and
                    (nr, nc) not in visited
                ):
                    heapq.heappush(minHeap, (grid[nr][nc], nr, nc))


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

        visited = {(0, 0)}
        # (depth, row, col)
        minHeap = [(grid[0][0], 0, 0)]
        ans = 0
        while minHeap:
            d, r, c = heapq.heappop(minHeap)
            # max depth encountered is total time taken
            # since at max time we can swim across this path in one go
            ans = max(ans, d)
            
            if r == c == N-1:
                return ans
            
            for cr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= cr < N and 0 <= cc < N and (cr, cc) not in visited:
                    heapq.heappush(minHeap, (grid[cr][cc], cr, cc))
                    visited.add((cr, cc))
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        min heap approach. add smallest num from 4 directions to queue
        keep visiting smallest till we reach bottom right.
        total time = max of the smallest elevations we encounter 

        '''
        N = len(grid)

        seen = {(0, 0)}
        minHeap = [(grid[0][0], 0, 0)]
        ans = 0
        while minHeap:
            d, r, c = heapq.heappop(minHeap)
            ans = max(ans, d)
            
            if r == c == N-1:
                return ans
            
            for cr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= cr < N and 0 <= cc < N and (cr, cc) not in seen:
                    heapq.heappush(minHeap, (grid[cr][cc], cr, cc))
                    seen.add((cr, cc))
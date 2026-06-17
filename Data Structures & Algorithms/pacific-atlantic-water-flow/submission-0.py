class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        Time complexity: O(m * n)
        Space complexity: O(m * n)
        '''
        nRows = len(heights)
        nCols = len(heights[0])

        pac = set()
        atl = set()

        def dfs(r , c, visited, prevHeight):
            if (r < 0 or r >= nRows or
                c < 0 or c >= nCols or
                (r, c) in visited or
                # condition for valid height = curr height >= prevHeight
                heights[r][c] < prevHeight
            ):
                return

            visited.add((r, c))
            
            # visit neighbors
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # start dfs from borders
        # condition for valid height = curr height >= prevHeight
        # then water from island can reach ocean
        for r in range(nRows):
            # find if pac can be reached
            dfs(r, 0, pac, heights[r][0])
            # find if atl can be reached
            dfs(r, nCols - 1, atl, heights[r][nCols - 1])
        
        for c in range(nCols):
            # find if pac can be reached
            dfs(0, c, pac, heights[0][c])
            # find if atl can be reached
            dfs(nRows - 1, c, atl, heights[nRows - 1][c])
        
        # O(min(set lens))
        return list(atl.intersection(pac))
        
        # OR
        
        # res = []
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if (r, c) in pac and (r, c) in atl:
        #             res.append([r, c])
        # return res
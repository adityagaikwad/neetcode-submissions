class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        Time : O(m * n)
        Space : O(m * n)
        '''
        memo = {}
        def dfs(r, c):
            if r >= m or c >= n:
                return 0
            
            if r == m - 1 and c == n - 1:
                return 1

            if (r, c) in memo:
                return memo[(r, c)]

            memo[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)

            return memo[(r, c)]

        return dfs(0, 0)

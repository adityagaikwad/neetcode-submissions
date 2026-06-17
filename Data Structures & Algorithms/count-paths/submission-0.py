class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        unique = 0
        def dfs(r, c):
            nonlocal unique

            if r >= m or c >= n:
                return
            
            if r == m - 1 and c == n - 1:
                unique += 1
            
            dfs(r + 1, c)
            dfs(r, c + 1)

        dfs(0, 0)
        return unique
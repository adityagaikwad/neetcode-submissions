class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        memo = {}
        def dfs(i, j):
            # reached end of either string
            if i == n1 or j == n2:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            res = 0
            if text1[i] == text2[j]:
                res = 1 + dfs(i + 1, j + 1)
            else:
                res = max(dfs(i + 1, j), dfs(i, j + 1))
            
            memo[(i, j)] = res

            return res
        
        return dfs(0, 0)
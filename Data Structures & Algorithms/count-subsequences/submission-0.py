class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        Time: O(m * n)
        Space: O(m * n)
        '''
        if len(t) > len(s):
            return 0

        memo = {}
        def dfs(i, j):
            # if we reach end of t, one possibility found.
            # return 1
            if j == len(t):
                return 1
            
            # if j is not at the end but i is, return 0
            if i == len(s):
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]

            # skip i'th char and see if you get any matches
            res = dfs(i + 1, j)

            # if the chars are equal, we can increment
            # and look for further char matches
            if s[i] == t[j]:
                # since we want total counts, we can add to existing res
                res += dfs(i + 1, j + 1)
            
            memo[(i, j)] = res

            return res

        return dfs(0, 0)


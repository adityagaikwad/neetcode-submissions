class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        Time: O(n * m)
            n = len s1
            m = len s2
        Space: O(n * m)
        '''
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}
        def dfs(i, j, k):
            # if s3 pointer has traversed complete string
            # check if s1 and s2 pointers have also traversed
            # complete string, else return False
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))

            if (i, j) in dp:
                return dp[(i, j)]

            res = False
            # if kth string matches s1[i], increment i and k ptrs
            if i < len(s1) and s1[i] == s3[k]:
                # s1[i] can be = s3[k] but only return true if possible from other strs
                # it can also be that s1[i] == s3[k] but future doesnt work
                # but s2[j] == s3[k] and s1[i] == s3[k + 1] or so on
                res = dfs(i + 1, j, k + 1)
            
            if not res and j < len(s2) and s2[j] == s3[k]:
                res = dfs(i, j + 1, k + 1)
            
            dp[(i, j)] = res
            return res

        return dfs(0, 0, 0)
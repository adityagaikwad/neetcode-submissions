'''
DFS over i, j, k and try to see if s1[i] == s3[k] or s2[j] == s3[k]
And increment corresponding pts to check next ptrs

Since we choose one or the other str it gurantees interleaving that way

Time: O(n * m)
    n = len s1
    m = len s2
Space: O(n * m)
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if n1 + n2 != n3:
            return False

        dp = {}
        
        def dfs(i, j, k):
            # only if i, j both reached end when k == n3 do we have complete s3
            if k == n3:
                return i == n1 and j == n2
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = False

            # if kth string matches s1[i], increment i and k ptrs else j and k ptrs
            res = (i < n1 and s1[i] == s3[k] and dfs(i + 1, j, k + 1)) or \
                  (j < n2 and s2[j] == s3[k] and dfs(i, j + 1, k + 1))
            
            dp[(i, j)] = res

            return res
        
        return dfs(0, 0, 0)


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # we know there's only one way to decode starting at n
        # since it's empty
        memo = {n: 1}

        def dfs(i):
            if i in memo:
                return memo[i]
            
            if s[i] == "0":
                return 0
            
            # get combos possible starting from i + 1
            res = dfs(i + 1)

            # if we are not at last num
            if i + 1 < n and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
            ):
                # it's a valid num, add starting from i + 2
                res += dfs(i + 2)
            
            memo[i] = res

            return res
        
        return dfs(0)
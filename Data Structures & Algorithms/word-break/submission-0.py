class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        Time: O(n*m*t)
            n = len(s)
            m = len(wordDict)
            t = maxLen in wordDict

            We do checks for each i from 0-n, check every word each time
            and max string comparison is t len
        Space: O(n)
            For each index max recursion stack

        For iterative start with dp[n] = True and go down
        '''
        memo = {len(s) : True}
        def dfs(i):
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                # if word len is less than valid s
                if ((i + len(w)) <= len(s) and 
                     s[i : i + len(w)] == w
                ):
                    # if it's possible to get a valid word from next idx
                    # then return true
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return dfs(0)
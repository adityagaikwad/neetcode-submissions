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
        n = len(s)

        def dfs(i):
            if i in memo:
                return memo[i]
            
            # check if we can get a valid word starting from idx i
            # against all words in wordDict
            for word in wordDict:
                m = len(word)
                if (i + m <= n) and s[i: i + m] == word:
                    # if it's possible to get a valid word from next idx
                    # then return true
                    if dfs(i + m):
                        memo[i] = True
                        return True
            
            memo[i] = False
            return False
        
        return dfs(0)
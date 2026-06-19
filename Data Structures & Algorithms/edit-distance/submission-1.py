class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        Time: O(n1 * n2)
        Space: O(n1 * n2)
        '''
        n1 = len(word1)
        n2 = len(word2)
        
        memo = {}
        def dfs(i, j):
            # Reached the end of word1. So the only way to match the 
            # rest of word2[j:] is to insert all remaining characters.
            if i == n1:
                return n2 - j
            
            # Reached end of word2, only way to match with word2 now is
            # to delete remaining chars in word1
            if j == n2:
                return n1 - i

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                # if equal, no need to perform any operation
                # go to next pointers for i, j
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                # if not equal, we get the min of all 3 options
                # 1. Delete char at i, so we check i + 1'th char with j'th char
                # 2. Insert at i, so we check i'th char with j + 1 now
                # 3. Replace char at i, so word1[i] is now equal to word2[j]
                #    Now we check i + 1 with j + 1.
                res = min(dfs(i + 1, j), dfs(i, j + 1))
                res = min(res, dfs(i + 1, j + 1))

                memo[(i, j)] = res + 1

            return memo[(i, j)]
        
        return dfs(0, 0)
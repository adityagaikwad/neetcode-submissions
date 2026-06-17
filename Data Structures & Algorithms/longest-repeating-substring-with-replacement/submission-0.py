class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Brute force
        Time complexity: O(n^2)
        Space complexity: O(m) where m is the total unique chars in string
        '''
        n = len(s)
        maxLen = 0

        for i in range(n):
            charMaxF = 0
            count = {}    
            for j in range(i, n):
                count[s[j]] = 1 + count.get(s[j], 0)
                charMaxF = max(charMaxF, count[s[j]])

                # check in current substring s[i: j + 1] if no. of chars left
                # after removing max freq char is <= k. Because then we can replace
                # all of these chars to match the most freq char
                if (j + 1 - i) - charMaxF <= k:
                    maxLen = max(maxLen, j + 1 - i)
        
        return maxLen
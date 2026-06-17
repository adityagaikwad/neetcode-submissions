class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Brute force
        Time complexity: O(n^2)
        Space complexity: O(m) where m is the total unique chars in string
        '''
        # n = len(s)
        # maxLen = 0

        # for i in range(n):
        #     charMaxF = 0
        #     count = {}    
        #     for j in range(i, n):
        #         count[s[j]] = 1 + count.get(s[j], 0)
        #         charMaxF = max(charMaxF, count[s[j]])

        #         # check in current substring s[i: j + 1] if no. of chars left
        #         # after removing max freq char is <= k. Because then we can replace
        #         # all of these chars to match the most freq char
        #         if (j + 1 - i) - charMaxF <= k:
        #             maxLen = max(maxLen, j + 1 - i)
        
        # return maxLen

        '''
        Sliding window
        Time complexity: O(m x n)
            Where m is the total unique chars in string
            n is the length of the string s
        Space complexity: O(m) 
        '''
        n = len(s)
        maxLen = 0

        charSet = set(s)

        for c in charSet:
            count = 0
            l = 0
            for r in range(n):
                if s[r] == c:
                    count += 1

                # current sliding window s[l: r + 1] - charCount if its greater than k,
                # then we need to shrink window so that at most k elements leaving current
                # char are in window, then we can replace all of them to match char
                # NOTE: Don't forget to reduce count of char when we slide window to right
                # as the chars go out of the window
                while (r + 1 - l) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                maxLen = max(maxLen, r + 1 - l)

        return maxLen

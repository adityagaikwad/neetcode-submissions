class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Brute force:
        Start a substring at every index and expand it one character at a time.
        Track the most frequent character in each substring.
        If the remaining characters can be replaced within k moves, update the answer.
        
        Time: O(n^2)
        Space: O(m)
            Where m is the total unique chars in string
            n is the length of the string s
        '''
        # n = len(s)
        # maxLen = 0

        # for i in range(n):
        #     charMaxF = 0
        #     count = {}

        #     for j in range(i, n):
        #         count[s[j]] = 1 + count.get(s[j], 0)
        #         charMaxF = max(charMaxF, count[s[j]])

        #         # Replace all characters except the most frequent one.
        #         # If that requires at most k replacements, this substring is valid.
        #         if (j + 1 - i) - charMaxF <= k:
        #             maxLen = max(maxLen, j + 1 - i)

        # return maxLen

        '''
        Sliding window for each target character:
        Try making the window all of one character c.
        Keep at most k characters in the window that are not c.
        Repeat this for every unique character and track the longest window.
        
        Time: O(m * n)
        Space: O(m)
            Where m is the total unique chars in string
            n is the length of the string s
        '''
        # n = len(s)
        # maxLen = 0

        # charSet = set(s)

        # for c in charSet:
        #     count = 0
        #     l = 0

        #     for r in range(n):
        #         if s[r] == c:
        #             count += 1

        #         # Window size - count of c = characters we need to replace.
        #         # Shrink until we need at most k replacements.
        #         while (r + 1 - l) - count > k:
        #             if s[l] == c:
        #                 count -= 1
        #             l += 1

        #         maxLen = max(maxLen, r + 1 - l)

        # return maxLen

        '''
        Sliding window (optimal):
        Track the frequency of characters in the current window.
        Keep the window if non-majority characters can be replaced within k moves.
        maxF may become stale after shrinking, but it never creates a larger wrong answer.
        
        Time: O(n)
        Space: O(m)
            Where m is the total unique chars in string
            n is the length of the string s
        '''
        n = len(s)
        maxLen = 0

        count = {}
        l = 0
        maxF = 0

        for r in range(n):
            count[s[r]] = 1 + count.get(s[r], 0)

            # Highest frequency seen while expanding the window.
            # maxF may be stale after shrinking, but a window of this length
            # was already valid earlier, so it cannot create a wrong maxLen
            maxF = max(maxF, count[s[r]])

            # Window size - maxF = replacements needed.
            # Shrink if we would need more than k replacements.
            while (r + 1 - l) - maxF > k:
                count[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r + 1 - l)

        return maxLen

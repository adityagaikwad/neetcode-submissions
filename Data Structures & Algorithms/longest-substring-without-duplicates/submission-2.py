class Solution:
    '''
    Sliding window approach

    l = 0, use r to move through the string, updating a map/hashset with char and its
    idx, so when r sees a char again, we know the max len for curr string has been
    reached. Only way to get new unique string start is at last pos curr repeated
    char was seen at + 1. 
    So if abcbjk is the string, when we get to second b we need to skip string till "ab.."
    and start from c to get cbjk as the new max len substring.

    Maintain a sliding window s[l:r + 1] with no duplicate characters.
    lastCharPosIdx stores each character's latest index. When a repeated 
    character is inside the window, move l just after its previous occurrence.

    Time: O(n)
    Space: O(m)
    
    n = len(s)
    m = max unique chars in s
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastCharPosIdx = {}

        maxLen = 0
        l = 0

        for r in range(len(s)):
            # If char was seen before, move l past its previous occurrence.
            # max ensures l never moves backward if that occurrence is
            # already outside the current window.
            if s[r] in lastCharPosIdx:
                l = max(l, lastCharPosIdx[s[r]] + 1)
            
            # s[l:r + 1] is now a valid substring without duplicates.
            maxLen = max(maxLen, r - l + 1)

            # Update char's most recent position.
            lastCharPosIdx[s[r]] = r
        
        return maxLen
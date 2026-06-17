'''
Sliding window

We keep on sliding window to right by 1, if the window char count has all
chars from t with same count, we shrink from left as long as tCharCount remains
same, then repeat till end of s.

Time complexity: O(n)
    n is length of s
Space complexity: O(m)
    m in number of total unique chars in s & t
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # frequency map of characters we need to match
        tCount = Counter(t)

        matchingSubstring = (-1, -1)
        matchingSubstringLen = float("inf")
        n = len(s)

        # number of unique chars fully satisfied in current window
        matchedCharCount = 0
        # total unique chars we need to satisfy
        neededCharCount = len(tCount)
        
        # frequency map of chars in current window
        substringCount = Counter()

        l = 0
        for r in range(n):
            substringCount[s[r]] += 1

            # a char becomes "satisfied" exactly when its window count reaches the required count
            if s[r] in tCount and substringCount[s[r]] == tCount[s[r]]:
                matchedCharCount += 1

            # all required chars are satisfied — try to shrink from the left
            while matchedCharCount == neededCharCount:
                # update best window before shrinking
                if r - l + 1 < matchingSubstringLen:
                    matchingSubstringLen = r - l + 1
                    matchingSubstring = (l, r)

                substringCount[s[l]] -= 1
                # if removing s[l] breaks the count for a required char, window is no longer valid
                if s[l] in tCount and substringCount[s[l]] < tCount[s[l]]:
                    matchedCharCount -= 1

                l += 1

        l, r = matchingSubstring
        return s[l: r + 1] if matchingSubstringLen != float("inf") else ""
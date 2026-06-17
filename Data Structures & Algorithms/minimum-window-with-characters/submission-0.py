from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Brute force

        Time complexity: O(n^2)
            n is length of s
        Space complexity: O(m)
            m in number of total unique chars in s & t
        '''

        # if t == "":
        #     return ""

        # tCount = Counter(t)

        # matchingSubstring = (-1, -1)
        # matchingSubstringLen = float("inf")
        # ns = len(s)

        # for l in range(ns):
        #     subStringCount = defaultdict(int)
        #     for r in range(l, ns):
        #         subStringCount[s[r]] += 1

        #         allCharsCountEqualOrGreater = True

        #         for c in tCount:
        #             if subStringCount[c] < tCount[c]:
        #                 allCharsCountEqualOrGreater = False
                
        #         if allCharsCountEqualOrGreater and (r - l + 1) < matchingSubstringLen:
        #             matchingSubstring = (l, r)
        #             matchingSubstringLen = r - l + 1
        
        # return s[matchingSubstring[0]: matchingSubstring[1] + 1] if matchingSubstringLen != float("inf") else ""

        '''
        Sliding window

        Time complexity: O(n)
            n is length of s
        Space complexity: O(m)
            m in number of total unique chars in s & t
        '''
        if t == "":
            return ""

        tCount = Counter(t)

        matchingSubstring = (-1, -1)
        matchingSubstringLen = float("inf")
        ns = len(s)

        matchedCountChar = 0
        neededCountChar = len(tCount)

        substringCount = defaultdict(int)

        l = 0
        for r in range(ns):
            substringCount[s[r]] += 1

            if s[r] in tCount and substringCount[s[r]] == tCount[s[r]]:
                matchedCountChar += 1
            
            while matchedCountChar == neededCountChar:
                if r - l + 1 < matchingSubstringLen:
                    matchingSubstring = (l, r)
                    matchingSubstringLen = r - l + 1

                # move left ahead to find smallest matching window
                substringCount[s[l]] -= 1
                if s[l] in tCount and substringCount[s[l]] < tCount[s[l]]:
                    matchedCountChar -= 1
                
                l += 1

        l, r = matchingSubstring
        return s[l: r + 1] if matchingSubstringLen != float("inf") else ""




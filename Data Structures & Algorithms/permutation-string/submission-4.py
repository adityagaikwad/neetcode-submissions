'''
Counter/HashMap

Time complexity: O(n x m)
    n is length of string 1, m is length of string 2
Space complexity: O(26) = O(1) 
'''
# from collections import defaultdict
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         count1 = defaultdict(int)
#         for c in s1:
#             count1[c] += 1

#         n2 = len(s2)
#         charNeeded = len(count1)

#         for i in range(n2):
#             count2 = defaultdict(int)
#             charCountMatched = 0

#             for j in range(i, n2):
#                 count2[s2[j]] += 1

#                 # one char has equal count in both substrings
#                 if count2[s2[j]] == count1[s2[j]]:
#                     charCountMatched += 1
                
#                 # if more char count than in s1, discard current substring
#                 if count2[s2[j]] > count1[s2[j]]:
#                     break

#                 if charCountMatched == charNeeded:
#                     return True
        
#         return False

'''
Counter with sliding window
Time complexity: O(n)
    n is length of string 2
Space complexity: O(n)
'''
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         n1, n2 = len(s1), len(s2)

#         if n1 > n2:
#             return False
        
#         # can also use python's Counter
#         count1 = [0]*26
#         count2 = [0]*26

#         # count first window before loop
#         # can also write a method to get pos instead of doing ord(s1[i]) - ord('a') everytime
#         for i in range(n1):
#             count1[ord(s1[i]) - ord('a')] += 1
#             count2[ord(s2[i]) - ord('a')] += 1
        
#         matches = 0
#         for i in range(26):
#             if count1[i] == count2[i]:
#                 matches += 1

#         # start sliding window
#         # our window size will always be len(s1) since we want
#         # to match complete permutation of s1 in s2's substring
#         l = 0
#         for r in range(n1, n2):
#             # if all 26 chars match between s1 and s2 substring
#             # i.e. complete substring match
#             if matches == 26:
#                 return True
            
#             indexR = ord(s2[r]) - ord('a')
#             count2[indexR] += 1

#             if count2[indexR] == count1[indexR]:
#                 matches += 1
#             # if by adding s2[r] to substring, we increased a
#             # s1=s2 char count by 1, we need to decrease matches by 1
#             elif count2[indexR] == count1[indexR] + 1:
#                 matches -= 1
            
#             indexL = ord(s2[l]) - ord('a')
#             # calculate matches updates for removing s2[l] from substring
#             count2[indexL] -= 1
#             if count2[indexL] == count1[indexL]:
#                 matches += 1
#             # if by removing s2[l] from the substring, we decreased a
#             # s1=s2 char count by 1, we need to decrease matches by 1
#             elif count2[indexL] == count1[indexL] - 1:
#                 matches -= 1
            
#             # to keep sliding window of size len(s1)
#             l += 1

#         return matches == 26

'''
Sliding window of fixed size len(s1) over s2.
Keep a Counter of s1 and the current window in s2.
Slide one character at a time: add the new right char, remove the
left char (delete key if count drops to zero to avoid ghost keys
breaking Counter equality). Check for match after every slide.

Time:  O(n2) — one pass over s2; each Counter comparison is O(26) = O(1)
Space: O(1)  — counters hold at most 26 keys
'''
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        c1 = Counter(s1)
        c2 = Counter(s2[:n1])  # first window

        start = 0
        for end in range(n1, n2):
            if c1 == c2:
                return True

            # remove left char; delete key if count hits zero so it doesn't
            # break Counter equality (Counter inherits dict.__eq__)
            c2[s2[start]] -= 1
            if c2[s2[start]] == 0:
                del c2[s2[start]]

            c2[s2[end]] += 1  # add new right char
            start += 1

        return c1 == c2  # check the final window
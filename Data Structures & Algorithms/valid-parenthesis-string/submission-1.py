'''
Time: O(n)
Space: O(n)
'''
# class Solution:
#     def checkValidString(self, s: str) -> bool:
#         left = []
#         star = []
#         for i, ch in enumerate(s):
#             if ch == '(':
#                 left.append(i)
#             elif ch == '*':
#                 star.append(i)
#             else:
#                 if not left and not star:
#                     return False
#                 if left:
#                     left.pop()
#                 else:
#                     star.pop()
        
#         while left and star:
#             if left.pop() > star.pop():
#                 return False
#         return not left

'''
Greedy range tracking

Instead of tracking one fixed open-bracket count, track the possible range
[leftMin, leftMax]. A valid wildcard assignment exists if and only if 0 is
reachable within that range by the end of the string.

leftMin = minimum possible unmatched '(' count (wildcards as ')' or empty)
leftMax = maximum possible unmatched '(' count (wildcards as '(')

Clamping leftMin to 0 is safe because wildcards do not have to be ')'.
Only leftMax going negative proves structural impossibility, since even the
best-case assignment could not absorb the excess ')'.

Time: O(n)
    Single pass through the string
Space: O(1)
    Two scalar counters regardless of input length
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin = leftMin + 1
                leftMax = leftMax + 1
            elif c == ")":
                leftMin = leftMin - 1
                leftMax = leftMax - 1
            else:
                leftMin = leftMin - 1  # wildcard as ')'
                leftMax = leftMax + 1  # wildcard as '('

            # even treating all wildcards as '(' can't absorb the excess ')'
            # we subtract leftMax on seeing a ')' only so excess found
            if leftMax < 0:
                return False

            # we just ignore the wildCard possibility of adding a ")" if
            # num of "(" is 0 already
            if leftMin < 0:
                leftMin = 0

        return leftMin == 0
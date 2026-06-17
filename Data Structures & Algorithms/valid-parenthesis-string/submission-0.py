class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        Time: O(n)
        Space: O(n)
        '''
        left = []
        star = []
        for i, ch in enumerate(s):
            if ch == '(':
                left.append(i)
            elif ch == '*':
                star.append(i)
            else:
                if not left and not star:
                    return False
                if left:
                    left.pop()
                else:
                    star.pop()
        
        while left and star:
            if left.pop() > star.pop():
                return False
        return not left

        '''
        Time: O(n) solution
        Space: O(1)
        '''
        # wildcard can introduce more parenthesis
        # leftMin tracks total possible min left brackets
        # if wildcard = ")"
        # leftMax tracks if wildcard = "("
        # leftMin, leftMax = 0, 0

        # for c in s:
        #     if c == "(":
        #         leftMin = leftMin + 1
        #         leftMax = leftMax + 1
        #     elif c == ")":
        #         leftMin = leftMin - 1
        #         leftMax = leftMax - 1
        #     # wildcard
        #     else:
        #         # wildcard = ")"
        #         leftMin = leftMin - 1
        #         # wildcard = "("
        #         leftMax = leftMax + 1

        #     # if leftMax ever goes negative, we cannot recover
        #     # since there weren't enough ")" along the way
        #     if leftMax < 0:
        #         return False
            
        #     # we just ignore the wildCard possibility of adding a ")" if
        #     # num of "(" is 0 already.
        #     if leftMin < 0:
        #         leftMin = 0
        
        # return leftMin == 0
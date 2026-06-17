class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(currStr, unclosedLeft, remainingN):
            if unclosedLeft > n:
                return
            if remainingN < 0:
                return

            if remainingN == 0 and unclosedLeft == 0:
                res.append(currStr)
                return
            if unclosedLeft > 0:
                backtrack(currStr + ")", unclosedLeft - 1, remainingN - 1)
            
            backtrack(currStr + "(", unclosedLeft + 1, remainingN)

        backtrack("", 0, n)
        return res
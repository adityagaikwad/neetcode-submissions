'''
Pass unclosedLeft and remainingN to backtrack along with currStr
remainingN = non closed parenthesis

Key rules for valid parentheses:

You can add '(' only if you still have openings left (open < n).
You can add ')' only if it won't break validity (close < open).

A string is complete and valid only when open == close == n
    Add to res then

Backtrack by adding ')' if unclosedLeft > 0 -> also do remainingN -= 1
Backtrack by adding '(' and do unclosedLeft += 1

Time: O(4^n/ sqrt(n))
    
    Simple: O(2^2n) -> without our optimizations for unclosedLeft etc
    2n is the len of final string, at each char we have two choices choosing
    '(' or ')'. 

    But what we are doing is F(n) = F(0)*F(n - 1) + F(1)*F(n - 2) + ... + F(n - 1)*F(0)
    Where F(i) is the count of valid parenthesis where n = i. So total valid =
    F(1)*F(n-1) sum since count of valid strs of 1 * count of valid strs of (n-1)
    give us one possible split to get a valid F(n) answer.

    Therefore, the n th Catalan numbers is precisely the number of ways to
    form valid combinations of n pairs of parentheses.
    
    nth catalan num can be calculated using ( 4^n/ sqrt(n) )

Space: O(n)
    Max depth of backtrack will be 2n
'''
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
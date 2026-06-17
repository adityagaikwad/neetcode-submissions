'''
Time: O(4^n * n)
    Worst case all digits are 7s and/or 9s which map to 4 chars
    So each digit has 4 options for char so 4^n
    and * n because of string concatenation currStr + ch max of O(n) per combination

Space: O(n) for currStr max
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        n = len(digits)

        def backtrack(startFrom, currStr):
            if startFrom >= n:
                res.append(currStr)
                return
            # IMP: No need to do for i in range(startFrom, n)
            # when we do backtrack of startFrom + 1 it takes care of that
            # if we do that for loop then for digits = 234 we may start new
            # backtracking from 3 and end at 4 leading to 2 chars instead of 3 in res
            digit = digits[startFrom]
            for ch in mapping[digit]:
                backtrack(startFrom + 1, currStr + ch)
        
        backtrack(0, "")
        return res
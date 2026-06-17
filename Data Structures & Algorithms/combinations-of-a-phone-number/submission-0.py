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
            
            digit = digits[startFrom]
            for ch in mapping[digit]:
                backtrack(startFrom + 1, currStr + ch)
        
        backtrack(0, "")
        return res
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ref = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        for bracket in s:
            if bracket in ref:
                stack.append(bracket)
            else:
                if not stack or bracket != ref[stack.pop()]:
                    return False
        
        return not stack
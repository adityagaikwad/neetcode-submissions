class Solution:
    '''
    For every "(" add ")" to the stack, when you see ")" see if stack top is ")"
    then pop, else return false
    '''
    def isValid(self, s: str) -> bool:
        stack = []

        complement = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for ch in s:
            if ch in complement:
                stack.append(complement[ch])
            else:
                if not stack or stack[-1] != ch:
                    return False
                stack.pop()
        
        return len(stack) == 0
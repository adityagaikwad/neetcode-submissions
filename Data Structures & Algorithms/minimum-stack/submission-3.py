'''
Track the current min value at every push (val, minSoFar)
So that when we pop, we still track new min easily

Time: O(1)
Space: O(n)
'''
class MinStack:

    def __init__(self):
        # value = (val, minSoFar)
        self.stack = []

    def push(self, val: int) -> None:
        minSoFar = None
        if self.stack:
            # val is lower
            if val < self.stack[-1][1]:
                minSoFar = val
            # stack top is lower
            else:
                minSoFar = self.stack[-1][1]                
        else:
            # empty stack, val is lowest
            minSoFar = val

        self.stack.append((val, minSoFar))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

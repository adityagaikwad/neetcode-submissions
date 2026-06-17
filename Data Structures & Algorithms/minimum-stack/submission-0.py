import heapq

class MinStack:

    def __init__(self):
        self.min = float("inf")
        self.stack = []
        # the below stack tracks the min upto index i
        # i.e for nums[:i] what is the min so far?
        self.minAtPosStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        minSoFar = min(
            val,
            self.minAtPosStack[-1] if self.minAtPosStack else val
        )

        self.minAtPosStack.append(minSoFar)

    def pop(self) -> None:
        self.stack.pop()
        self.minAtPosStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minAtPosStack[-1]
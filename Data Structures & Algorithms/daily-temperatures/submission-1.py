"""
Goal: for each day, find how many days until a warmer temperature.
Brute force scans forward from each day — O(n²).
Stack approach resolves past days lazily as we scan forward — O(n).

We keep a stack of "unresolved" days (days still waiting for a warmer day).
The stack is always monotonically decreasing from bottom to top because:
  - we only keep a day if it hasn't found a warmer future day yet
  - a warmer day would have popped it already

Original if/else logic:
  if stack is empty:
    nothing to compare against, push current day as unresolved
  elif curr temp <= stack top:
    current day is cooler/equal, so stack top is still unresolved
    push current day as unresolved too (it also needs a future warmer day)
  else (curr temp > stack top):
    current day is warmer than stack top — stack top has found its answer
    pop it and record gap (current index - popped index) in result
    keep popping while current temp is still warmer (one day can be the
    answer for multiple past days)
    then push current day as unresolved (it may still need a future warmer day)

Simplified: `while stack and stack[-1][0] < t` collapses all three branches.
  - empty stack: while condition is false, skip to append
  - curr <= top: while condition is false, skip to append
  - curr > top: pop and record, then append
Days remaining in the stack at the end never found a warmer day, so result
stays 0 for them (initialized to 0).
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []

        res = [0] * n

        for idx, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, idx))
            else:
                # did not find increasing temp
                if temp < stack[-1][0]:
                    stack.append((temp, idx))
                # found increasing temp in future
                # pop all smaller temps and add dist to res
                else:
                    while stack and temp > stack[-1][0]:
                        smallerTemp, oldIdx = stack.pop()
                        # add days to warm temp to res
                        res[oldIdx] = idx - oldIdx

                    # add new temp to stack
                    stack.append((temp, idx))
        
        return res

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        # monotonically decreasing stack of (temp, index)
        # simpler approach: no if/else needed — the while condition
        # handles both the empty stack and the "not warmer" cases
        stack = []

        res = [0] * n

        for i, t in enumerate(temperatures):
            # pop all stack entries cooler than current temp
            # and record how many days it took to reach a warmer day
            while stack and stack[-1][0] < t:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx

            # always push current temp — it hasn't found a warmer day yet
            stack.append((t, i))

        return res
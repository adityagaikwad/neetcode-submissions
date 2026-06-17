class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        # monotonically decreasing stack
        # where leftmost value is max
        # we pop till curr element is greater than any existing elements
        stack = []
        
        res = [0] * n

        for i, t in enumerate(temperatures):
            # 2. when a curr temp is > smallest temp in stack
            # i.e stack[-1], we pop all such temps and record
            # the days to reach warmer temp in the res[old_idx]
            while stack and stack[-1][0] < t:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            # 1. we add to all temps to stack
            stack.append((t, i))
        
        return res

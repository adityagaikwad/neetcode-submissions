'''
Monotonic stack.

For each bar, we want to know the largest rectangle where it is the
shortest bar (since the shortest bar limits the height of any rectangle).

We use a stack to track bars in increasing height order, storing
(start_index, height) for each. start_index is how far left that
height can currently reach.

At each step:
    - If current height >= stack top, push and move on.
    - If current height < stack top, the taller bar on top cannot
    extend to the right anymore. So pop it and compute its area:

        area = height * (current_index - start_index)

    Keep popping all bars taller than the current one, since none
    of them can extend forward either.
    - The current bar can stretch back to the start_index of the
    last popped bar, so we reuse that as its own start_index.

Diagram for heights = [7, 1, 7, 2]:

    7       7
    7       7
    7   7   7
    7   7   7   2
    7   7   7   2
    7 1 7 2 7 2 2 2   ← extended widths
    0   1   2   3

    At i=1 (h=1): pop (0,7) → area = 7*1 = 7. start carries back to 0.
    At i=3 (h=2): pop (2,7) → area = 7*1 = 7. start carries back to 2.

After the loop, remaining bars in the stack have no right boundary,
so they extend to the end of the array.

Time complexity: O(n)
    Each bar is pushed and popped at most once
Space complexity: O(n)
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # (index, height)
        n = len(heights)

        for i, h in enumerate(heights):
            start = i
            # if curr is lower, prev height cannot extend anymore
            # pop it and calculate area
            while stack and h < stack[-1][1]:
                startIdx, height = stack.pop()
                maxArea = max(maxArea, height * (i - startIdx))

                # since we popped some elements which were bigger than h
                # when we calculate area for heights[i]
                # we use the index of the element farthest away and longer than i
                start = startIdx
            
            stack.append((start, h))
        
        for i, h in stack:
            # all remaining elements can extend their height
            # till the end for max area
            maxArea = max(maxArea, h * (n - i))

        return maxArea

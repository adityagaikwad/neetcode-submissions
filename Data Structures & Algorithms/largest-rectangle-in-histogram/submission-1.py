class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # (index, height)

        for i, h in enumerate(heights):
            start = i
            # if we encounter a height smaller than the 
            # top element in stack, we pop and calculate its area
            # since it cannot extend at that height anymore
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
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
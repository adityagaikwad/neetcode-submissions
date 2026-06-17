class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxSoFar = 0
        n = len(heights)
        l = 0
        r = n - 1

        while l < r:
            currArea = min(heights[l], heights[r]) * (r - l)
            maxSoFar = max(maxSoFar, currArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxSoFar
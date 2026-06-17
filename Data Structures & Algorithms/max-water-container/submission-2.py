class Solution:
    '''
    We are limited by height for the area so init two pointers one at each end
    Then calculate area and compare with max, then move the smaller height ptr
    inwards. so l+=1 or r-=1 whichever is smaller and calculate area each time

    Time: O(n)
    Space: O(1)
    '''
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
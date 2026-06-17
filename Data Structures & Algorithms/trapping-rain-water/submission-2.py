class Solution:
    '''
    Two arrays approach

    At any pos i, water trapped = min (maxLeftHeight[i], maxRightHeight[i]) - height[i]
    fill the two arrs, then calculate area trapped per height

    Time: O(n)
    Space: O(n)
    '''
    # def trap(self, height: List[int]) -> int:
    #     n = len(height)
    #     maxLeft = [0] * n
    #     maxRight = [0] * n

    #     maxLeft[0] = height[0]
    #     for i in range(1, n):
    #         maxLeft[i] = max(maxLeft[i - 1], height[i])
        
    #     maxRight[n - 1] = height[n - 1]
    #     for i in range(n - 2, -1, -1):
    #         maxRight[i] = max(maxRight[i + 1], height[i])
        

    #     totalArea = 0
    #     for i in range(n):
    #         currArea = min(maxLeft[i], maxRight[i]) - height[i]
    #         totalArea += currArea

    #     return totalArea

    '''
    Two pointers without extra arr approach -
    
    Water at a position is limited by the smaller of its tallest left and right 
    boundaries. If leftMax < rightMax, the left side is the limiting boundary,
    so we calculate water at height[l]. Otherwise, rightMax is the limiting
    boundary, so we calculate water at height[r].
    '''
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                # rightMax is taller, so leftMax determines the water level on the left.
                l += 1
                leftMax = max(leftMax, height[l])
                # calculate water only at height[l]
                res += leftMax - height[l]
            else:
                # leftMax is taller or equal, so rightMax determines the water level on the right.
                r -= 1
                rightMax = max(rightMax, height[r])
                # calculate water only at height[r]
                res += rightMax - height[r]

        return res






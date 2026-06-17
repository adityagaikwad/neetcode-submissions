class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        largestOnRight = [0] * n
        largestOnLeft = [0] * n

        largestOnR = height[n - 1]
        for i in range(n - 2, -1, -1):
            largestOnRight[i] = largestOnR
            largestOnR = max(largestOnR, height[i])

        largestOnL = height[0]
        for i in range(1, n):
            largestOnLeft[i] = largestOnL
            largestOnL = max(largestOnL, height[i])
        
        totalWater = 0
        for i in range(n):
            waterAtI = min(largestOnLeft[i], largestOnRight[i]) - height[i]

            if waterAtI > 0:
                totalWater += waterAtI
        
        return totalWater
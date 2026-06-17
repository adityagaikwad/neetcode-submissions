class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minLeft = prices[0]

        maxP = 0
        for i in range(1, len(prices)):
            if minLeft < prices[i]:
                maxP = max(maxP, prices[i] - minLeft)
            else:
                minLeft = prices[i]
        
        return maxP
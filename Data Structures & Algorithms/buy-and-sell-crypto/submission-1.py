class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        minBuyPrice = prices[0]
        profit = 0

        for sellPrice in prices[1:]:
            profit = max(profit, sellPrice - minBuyPrice)
            minBuyPrice = min(minBuyPrice, sellPrice)
        
        return profit
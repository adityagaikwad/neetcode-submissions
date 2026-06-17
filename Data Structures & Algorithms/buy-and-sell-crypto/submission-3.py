class Solution:
    '''
    Time: O(n)
    Space: O(1)
    '''
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        minBuyPrice = prices[0]
        profit = 0

        for sellPrice in prices[1:]:
            profit = max(profit, sellPrice - minBuyPrice)
            minBuyPrice = min(minBuyPrice, sellPrice)
        
        return profit
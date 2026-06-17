class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''

        if not prices:
            return 0
        
        n = len(prices)
        memo = {}

        def dfs(i, canBuy):
            # cannot buy at day = i or further
            if i >= n:
                return 0

            if (i, canBuy) in memo:
                return memo[(i, canBuy)]

            # Option 1: cooldown — skip today and keep the same state (no buying or selling)
            cooldownProfit = dfs(i + 1, canBuy)
            
            if canBuy:
                # buy on i'th day + dfs(i + 1, cannot buy next day)
                buyProfit = dfs(i + 1, False) - prices[i]
                memo[(i, canBuy)] = max(buyProfit, cooldownProfit)
            # cannot buy, but can sell today
            else:
                # profit from selling coin today
                # + (cooldown for i + 1 day i.e can buy on i
                #  + 2, True coz can buy on i + 2)
                sellProfit = dfs(i + 2, True) + prices[i]
                memo[(i, canBuy)] = max(sellProfit, cooldownProfit)

            return memo[(i, canBuy)]

        return dfs(0, True)
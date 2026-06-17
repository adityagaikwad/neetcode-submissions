class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        Time: O(n * amount)
            We do dfs once for each (i, remainingAmount)
        Space: O(n * amount)
        '''
        memo = {}

        def dfs(i, remainingAmount):
            if remainingAmount == 0:
                return 1
            if i >= len(coins):
                return 0
            if (i, remainingAmount) in memo:
                return memo[(i, remainingAmount)]
            
            # skip current coin and try with next coin
            res = dfs(i + 1, remainingAmount)
            
            # if coin is smaller than remaining amount only
            # then it makes sense to even explore that path
            if remainingAmount >= coins[i]:
                res += dfs(i, remainingAmount - coins[i])

            memo[(i, remainingAmount)] = res
            return res

        return dfs(0, amount)
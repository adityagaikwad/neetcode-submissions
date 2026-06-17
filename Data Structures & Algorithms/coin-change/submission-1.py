'''
Recursive DFS with memoization

Define dfs(amount) as the minimum number of coins needed to reach exactly amount.
At each call, try subtracting every denomination and recurse on the remainder,
taking 1 plus the minimum result across all valid choices (those that keep the
remainder non-negative). Memoizing each subproblem collapses the exponential
recursion tree to at most t unique states, one per remainder value from 0 to amount.

Time: O(n * t)
    t unique subproblems (one per amount from 0 to t), each scanning all n coins
Space: O(t)
    Memo dict holds at most t + 1 entries; call stack depth reaches t in the
    worst case when only denomination 1 is available
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            res = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            
            memo[amount] = res
            return res
        
        minCoins = dfs(amount)
        return -1 if minCoins >= float("inf") else minCoins
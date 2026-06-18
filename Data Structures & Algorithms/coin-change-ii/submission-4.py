'''
Memoized DFS (top-down DP)

At each index i, we either skip coins[i] (advance to i+1) or use it (stay at i).
Staying at i allows unlimited reuse of the same denomination, while never going back
to a smaller index enforces non-decreasing selection order. Each valid multiset has
exactly one path through the recursion tree, so no combination is counted twice.

i = current coin index; coins[i] and all higher-index coins are still available
remainingAmount = how much more is needed to reach amount

Time: O(n * amount)
    Each (i, remainingAmount) pair is computed once; there are n * amount unique pairs
Space: O(n * amount)
    Memo table holds n * amount entries; call stack depth is also bounded by n * amount
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
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
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

'''
Bottom-up DP

Process one coin denomination at a time, building a fresh nextDP for each pass.
dp[a] holds the count from the previous pass (coins[i+1] onward); nextDP[a] extends
that by deciding what to do with coins[i].

Two choices at each amount a, mirroring the memoized DFS:
- skip coins[i]: inherit dp[a] directly
- use coins[i]:  add nextDP[a - coins[i]] (reads from nextDP, not dp)

Reading nextDP for the use branch is why unlimited reuse works: nextDP[a - coins[i]]
already accounts for earlier uses of coins[i] within the same pass. Iterating coins
right to left enforces the same ordering constraint as the DFS so each combination
is counted exactly once.

Example: coins = [1, 2], amount = 3
    Start:  dp = [1, 0, 0, 0]
    i=1 (coin=2): nextDP = [1, 0, 1, 0]   # [2] is the only reachable combination
    i=0 (coin=1): nextDP = [1, 1, 2, 2]   # [1], [1,1] or [2], [1,1,1] or [1,2]

Time: O(n * amount)
    Each of the n coins triggers one full pass over the amount+1 array
Space: O(amount)
    Only two arrays of size amount+1 exist at once; old dp is discarded each iteration
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] stores the num ways to get amount i from existing coins
        dp = [0] * (amount + 1)
        # only one way get amount=0
        dp[0] = 1

        # start with largest coin first
        for i in range(len(coins) - 1, -1, -1):
            # use a copy and update with dp[a] details
            nextDp = [0] * (amount + 1)
            nextDp[0] = 1

            for a in range(1, amount + 1):
                # skip coins[i] to get to amount=a
                nextDp[a] = dp[a]

                # use coins[i] to get to a
                # ways to dp[a] = skip + use coin = dp[a] + nextDp[a - coins[i]]
                # use nextDp here because we updated it on lower amount in this round
                if a - coins[i] >= 0:
                    nextDp[a] += nextDp[a - coins[i]]
            
            dp = nextDp
        
        return dp[amount]








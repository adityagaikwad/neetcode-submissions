class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        # We can start at step 0 or step 1 without paying any cost yet.
        # So dp[0], dp[1] = 0

        # At each stair i, you must have come from either:
        #   stair i - 1, or
        #   stair i - 2
        for i in range(2, n + 1):
            # min(cost to reach i-1 + cost of stepping on i-1,
            # cost to reach i-2 + cost of stepping on i-2)
            dp[i] = min(
                dp[i - 1] + cost[i - 1],
                dp[i - 2] + cost[i - 2]
            )
        
        return dp[n]
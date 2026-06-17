class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [0] * (n + 1)

        # dp[i] = max val including house i
        dp[n] = 0
        # include last house
        dp[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i + 2] + nums[i], dp[i + 1])

        return dp[0]
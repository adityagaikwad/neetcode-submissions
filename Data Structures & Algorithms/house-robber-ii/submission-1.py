class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # either skip the first house or skip the last house
        # no solution can include both
        return max(self.rob_simple(nums[1:]), self.rob_simple(nums[:-1]))

    def rob_simple(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)

        dp = [0] * (n + 1)

        dp[n] = 0
        dp[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i + 2] + nums[i], dp[i + 1])
        
        return dp[0]
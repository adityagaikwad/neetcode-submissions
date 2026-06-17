class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # either skip the first house or skip the last house
        # no solution can include both
        return max(self.rob_simple(nums[1:]), self.rob_simple(nums[:-1]))

    def rob_simple(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        dp = [0] * (n)
        # max of robbing upto 1 house is that house
        dp[0] = nums[0]
        # max of robbing upto 2 houses is max of either house
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # rob 2 house before and curr or prev neighbor which is higher
            dp[i] = max(
                dp[i - 2] + nums[i],
                dp[i - 1]
            )
        
        return dp[n - 1]
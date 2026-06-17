'''
Time: O(n)
Space: O(n)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        
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

'''
two pointers, rob1 and rob2 pointing to one house before curr
and 2 houses before curr

either rob 2 houses before curr and then curr (skip prev neighbor) or currMax
is by robbing prev neighbor
currMax = max(rob1 + curr, rob2)

Time: O(n)
Space: O(1)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
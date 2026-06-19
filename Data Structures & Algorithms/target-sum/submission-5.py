class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        Time: O(n * m)
            n = len nums
            m = sum of nums
        Space: O(n * m)
        '''
        memo = {}
        n = len(nums)

        def dfs(i, currTotal):
            if i >= n:
                return 1 if currTotal == target else 0
            
            if (i, currTotal) in memo:
                return memo[(i, currTotal)]
            
            memo[(i, currTotal)] = dfs(i + 1, currTotal + nums[i]) +\
                                   dfs(i + 1, currTotal - nums[i])
            
            return memo[(i, currTotal)]
        
        return dfs(0, 0)

'''
Bottom-up DP (iterative, hash map)

dp maps each reachable sum to the number of ways to reach it using numbers processed so far.
At each step, every existing sum branches into two new sums by adding or subtracting the
current number. Counts accumulate when multiple paths arrive at the same sum.

dp[s] = number of ways to reach sum s using all numbers processed so far

Time: O(n * S) where S = sum(nums)
    Each number iterates over at most 2S+1 reachable sums in dp
Space: O(S)
    dp holds at most 2*sum(nums)+1 entries at once; next_dp replaces dp each iteration
'''
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         # dp[i] = num ways to get amount dp[i][amount] using first i nums
#         # dp gets updated after every new num gets checked
#         dp = defaultdict(int)
#         dp[0] = 1

#         for num in nums:
#             next_dp = defaultdict(int)
#             for total in dp:
#                 # ways to get to total + num = ways to get to total
#                 # since we are adding/subtracing just num, total count stays same
#                 # each path that reached total extends unchanged: +num and -num are the only choices
#                 next_dp[total + num] += dp[total]
#                 next_dp[total - num] += dp[total]
            
#             dp = next_dp

#         return dp[target]


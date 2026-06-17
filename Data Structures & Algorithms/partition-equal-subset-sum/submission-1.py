'''
First check if total % 2 == 0 so its divisible into two sets

Then, check if you can use some nums to get total/2 sum with DFS

Time: O(n * target)
      We go over n total nums for remaining sum from 1 to target/2 times worst case

Space: O(n * target)
       memo size
'''
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         n = len(nums)
#         memo = {}

#         def dfs(remainingSum, startFrom):
#             if remainingSum == 0:
#                 return True
            
#             if (remainingSum, startFrom) in memo:
#                 return memo[(remainingSum, startFrom)]
            
#             if startFrom == n or remainingSum < 0:
#                 return False
            
#             res = dfs(remainingSum - nums[startFrom], startFrom + 1) or \
#                   dfs(remainingSum, startFrom + 1)
            
#             memo[(remainingSum, startFrom)] = res

#             return res

#         totalSum = sum(nums)

#         if totalSum % 2 != 0:
#             return False
        
#         return dfs(totalSum/2, 0)

'''
1D DP (0/1 knapsack)

We reduce the problem to: can any subset of nums sum to target = total/2?
dp[j] = True means we can form sum j using some subset of nums seen so far.
For each num we scan j downward from target to num, setting dp[j] = dp[j] or dp[j-num].
This asks: can we reach sum j either without using num (dp[j] unchanged) or by
adding num to a subset that already summed to j-num?

Scanning backwards is critical: it ensures each num is used at most once per pass.
Scanning forward would let dp[j-num] already reflect the current num being added,
effectively counting it twice.

Worked example with nums = [1, 2, 3, 4], total = 10, target = 5:
    Start: dp = [T, F, F, F, F, F]
    num=1: dp = [T, T, F, F, F, F]   sums reachable: {0, 1}
    num=2: dp = [T, T, T, T, F, F]   sums reachable: {0, 1, 2, 3}
    num=3: dp = [T, T, T, T, T, T]   sums reachable: {0, 1, 2, 3, 4, 5}
    dp[5] is True, so a valid partition exists.

Time: O(n * target)
    For each of n elements we iterate over at most target indices
Space: O(target)
    dp array has target+1 entries, no other scaling structure
'''
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)

        # the empty subset sums to 0, so sum 0 is always reachable
        dp[0] = True
        for num in nums:
            # traverse right to left so num is never used twice in one pass
            for j in range(target, num - 1, -1):
                # can we reach j by adding num to a subset that already summed to j-num?
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
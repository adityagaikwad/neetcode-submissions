class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}

        def dfs(remainingSum, startFrom):
            if remainingSum == 0:
                return True
            
            if (remainingSum, startFrom) in memo:
                return memo[(remainingSum, startFrom)]
            
            if startFrom == n or remainingSum < 0:
                return False
            
            res = dfs(remainingSum - nums[startFrom], startFrom + 1) or dfs(remainingSum, startFrom + 1)
            memo[(remainingSum, startFrom)] = res

            return res

        totalSum = sum(nums)

        if totalSum % 2 != 0:
            return False
        
        return dfs(totalSum/2, 0)
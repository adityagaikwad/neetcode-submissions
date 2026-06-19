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

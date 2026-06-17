class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        Time: O(n * m)
            n = len nums
            m = sum of nums
        Space: O(n * m)
        '''
        n = len(nums)

        dp = {}  # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            # consider -ve and +ve for nums[i] and sum the counts
            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) + 
                              backtrack(i + 1, total - nums[i]))
            return dp[(i, total)]

        return backtrack(0, 0)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        memo = {}
        def dfs(i, prevNum):
            if i == n:
                return 0

            if (i, prevNum) in memo:
                return memo[(i, prevNum)]
            
            # do not include curr num
            res = dfs(i + 1, prevNum)
            
            # include curr num
            if nums[i] > prevNum:
                res = max(res, 1 + dfs(i + 1, nums[i]))

            memo[(i, prevNum)] = res
            return res

        return dfs(0, float("-inf"))
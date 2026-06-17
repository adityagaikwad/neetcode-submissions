class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        '''
        Basic recursion without DP
        '''
        # nums = [1] + nums + [1]

        # def dfs(nums):
        #     if len(nums) == 2:
        #         return 0

        #     maxCoins = 0
        #     for i in range(1, len(nums) - 1):
        #         coins = nums[i - 1] * nums[i] * nums[i + 1]
        #         coins += dfs(nums[:i] + nums[i + 1:])
        #         maxCoins = max(maxCoins, coins)
        #     return maxCoins

        # return dfs(nums)

        '''
        Recursion with DP
        Time: O(n^3)
            for all l, r it takes O(n^2) time then for each such dfs
            call, we iterate over l to r i.e O(n) more
        Space: O(n^2)
            for all l, r it takes O(n^2) recursion stack worst case
        '''
        nums = [1] + nums + [1]
        
        memo = {}
        def dfs(l, r):
            if l > r:
                return 0
            
            if (l, r) in memo:
                return memo[(l, r)]
            
            maxCoins = 0
            # Try bursting each balloon in the range [l, r] last,
            # and recursively solve the left and right sides
            for i in range(l, r + 1):
                # Coins gained by bursting balloon i last in this range
                # We do the recursive calls first so only
                # nums[i] and nums[l - 1] and nums[r + 1] are left next to nums[i]
                # burst them
                coins = nums[l - 1] * nums[i] * nums[r + 1]

                # Add coins from solving the subproblems on left and right
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                maxCoins = max(maxCoins, coins)
            
            memo[(l, r)] = maxCoins
            
            return maxCoins
        
        return dfs(1, len(nums) - 2)

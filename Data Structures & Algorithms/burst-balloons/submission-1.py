'''
Interval DP with memoization (top-down)

For a range l, r in nums, choose which balloon to burst last
do a for loop for i in range(l, r) and assume you burst i last
so coins[i] = nums[l - 1] * nums[i] * nums[r + 1] aka all others in l to r have
been burst already.

For the remaining balloons, the coins += dfs(l, i - 1) + dfs(i + 1, r)
So total coins = coins from bursting i and two recursive burstings left and right
of balloon i

Time: O(n^3)
    O(n^2) distinct (l, r) subproblems; each iterates over O(n)
    choices for the last balloon to burst
    
    Count all valid pairs:

    (1,1), (1,2), (1,3), ..., (1,n)    →  n pairs
        (2,2), (2,3), ..., (2,n)    →  n-1 pairs
                (3,3), ..., (3,n)    →  n-2 pairs
                            ...
                            (n,n)    →  1 pair

    Total = n + (n-1) + ... + 1 = n(n+1)/2 = O(n^2).
    for all l, r it takes O(n^2) time then for each such dfs
    call, we iterate over l to r i.e O(n) more

Space: O(n^2)
    for all l, r it takes O(n^2) recursion stack worst case
'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
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

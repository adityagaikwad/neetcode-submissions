'''
Iterative DP - Bottom up approach

O(n) Time and Space
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        # dp is always 1 indexed
        dp = [0 for _ in range(n + 1)]
        # 1 way to reach step 1
        dp[1] = 1
        # 2 ways to reach step 2, [1,1] or [2]
        dp[2] = 2

        for i in range(3, n + 1):
            # can reach dp[i] from either two 1 steps from i - 1
            # or one step of 2 from i - 2 
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

'''
Iterative DP, bottom-up (space-optimized Fibonacci)

Climbing stairs follows the Fibonacci recurrence: the number of ways to reach
step i equals ways(i-1) + ways(i-2), because you can arrive from one step below
or two steps below. Rather than storing the full DP table, two variables roll
forward through the sequence and discard everything older than two positions back.

one = dp[i-1], the last computed value
two = dp[i-2], the value before that

Both initialize to 1 to represent the two base cases: being at the top (0 steps
left, 1 way) and being one step from the top (1 step left, 1 way).

Trace for n=4:
    Start:  one = dp[1] = 1,  two = dp[0] = 1

    i=0:  dp[2] = dp[1] + dp[0] = 2   (one = one + two = 1 + 1 = 2)  ->  one = 2,  two = 1
    i=1:  dp[3] = dp[2] + dp[1] = 3   (one = one + two = 2 + 1 = 3)  ->  one = 3,  two = 2
    i=2:  dp[4] = dp[3] + dp[2] = 5   (one = one + two = 3 + 2 = 5)  ->  one = 5,  two = 3

    return one = 5

Time: O(n)
    Single pass through n-1 iterations, each doing constant work
Space: O(1)
    Only two scalar variables maintained regardless of input size
'''
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         one, two = 1, 1

#         for i in range(n - 1):
#             temp = one
#             one = one + two
#             two = temp

#         return one

'''
Recursive DP with memoization, top-down

dfs(i) returns the number of distinct ways to reach step n starting from step i.
At each position, two recursive branches explore taking 1 step (land on i+1) or
taking 2 steps (land on i+2), and their results are summed. Each subproblem is
cached by step index so it is solved at most once.

dfs(i) = dfs(i+1) + dfs(i+2) because this approach counts paths forward from i
toward n. You have two choices at step i: take 1 step or take 2 steps. Each choice
spawns an independent subproblem, and the total paths from i is the sum of both.
This is the mirror of the bottom-up recurrence dp[i] = dp[i-1] + dp[i-2], which
counts paths arriving at i from behind. Here the branching goes the other direction:
outward from i, not backward into i.

Base case: i >= n returns i == n so only paths that land exactly on step n count
as valid. Paths that overshoot return 0 and contribute nothing to the sum.

Time: O(n)
    Each of the n steps is computed once and cached; all repeat calls return immediately
Space: O(n)
    Cache array of size n plus call stack up to depth n in the worst case
'''
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         cache = [-1 for _ in range(n)]

#         def dfs(i):
#             if i >= n:
#                 # when =n return 1 if higher return 0
#                 return i == n
            
#             if cache[i] != -1:
#                 return cache[i]
            
#             cache[i] = dfs(i + 1) + dfs(i + 2)
            
#             return cache[i]
        
#         return dfs(0)

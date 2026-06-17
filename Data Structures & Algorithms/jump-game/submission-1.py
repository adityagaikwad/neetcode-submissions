'''
Start from rightmost pos, ignore the jump at last idx coz we need to reach here,
nowhere to jump from here.

Then set leftmostReachablePos = n - 1, we go from right to left and at each idx
we see if we can reach the curr leftmostReachablePos from i,
aka i + nums[i] >= leftmostReachablePos
if so, then new leftmostReachablePos = i

So we keep going till the end and return leftmostReachablePos == 0

Time: O(n)
Space: O(1)
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        leftmostReachablePos = n - 1

        for i in range(n - 2, -1, -1):
            jump = nums[i]
            # we can reach curr leftmostReachablePos from i
            # so update leftmostReachablePos to i
            if i + jump >= leftmostReachablePos:
                leftmostReachablePos = i
        
        return leftmostReachablePos == 0


        
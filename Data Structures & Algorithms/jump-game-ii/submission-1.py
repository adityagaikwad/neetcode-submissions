'''
At each step calculate what is the farthest we can go when we get to
curr farthest, we jump then recalculate farthest and jump
we do not want to jump from the last element so skip it

Time: O(n)
Space: O(1)
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        end = 0
        minJumps = 0

        # skip last coz nowhere to jump from here
        for i, jump in enumerate(nums[:-1]):
            farthest = max(farthest, i + jump)

            # have to jump coz we did max jump already and got till i
            if i == end:
                end = farthest
                minJumps += 1
        
        return minJumps

class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        minJumps = 0
        end = 0

        # at each step calculate what is the farthest we can go
        # when we get to curr farthest, we jump
        # then recalculate farthest and jump
        # we do not want to jump from the last element so skip it
        for i, jump in enumerate(nums[:-1]):
            farthest = max(farthest, i + jump)

            if i == end:
                minJumps += 1
                end = farthest
        
        return minJumps

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            # if we can jump from i to go till or beyond goal,
            # go to prev idxs and check if they can reach i
            if i + nums[i] >= goal:
                goal = i

        # check if we were able to reach i = 0
        return goal == 0

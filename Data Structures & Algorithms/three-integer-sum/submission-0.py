from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        
        for i in range(n):
            # if the first number of sorted nums is positive
            # sum of all 3 will not be 0 for all following nums too
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # two sum
            l = i + 1
            r = n - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]    
                if threeSum > 0:
                    # need smaller numbers
                    r -= 1
                elif threeSum < 0:
                    # need bigger numbers
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicates from left
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # skip duplicates from right
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res

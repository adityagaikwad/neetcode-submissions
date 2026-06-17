'''
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        nSum = sum([i for i in range(n + 1)])

        return nSum - sum(nums)
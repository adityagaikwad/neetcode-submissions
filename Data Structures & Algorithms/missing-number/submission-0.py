class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = n

        for i in range(n):
            # n ^ n = 0 always
            # so by the end of the for loop
            # only the missing num will be in xor
            xor = xor ^ i ^ nums[i]
        
        return xor
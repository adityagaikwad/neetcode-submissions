'''
Total sum of 0 to n minus sum(nums)
Time: O(n)
Space: O(1)
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        nSum = sum([i for i in range(n + 1)])

        return nSum - sum(nums)

'''
a XOR a = 0
a XOR 0 = a

So we XOR all num in nums with i in range n
what's left is the missing num.

Time: O(n)
Space: O(1)
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # we for loop for 0 to n-1 so start with n
        # if n in nums it goes to 0, if not we know n is missing
        xor = n

        for i in range(n):
            # n ^ n = 0 always
            # so by the end of the for loop
            # only the missing num will be in xor
            xor = xor ^ i ^ nums[i]
        
        return xor
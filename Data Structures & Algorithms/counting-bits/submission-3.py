'''
DP with power-of-2 offset

Every integer i can be written as offset + remainder, where offset is the largest
power of 2 that is <= i. eg. for 3 would be 2 + 1 where 2 is the offset, 1 is remainder
The bit count of i is then 1 (for the leading bit at
offset) plus the bit count of (i - offset), which has already been computed and
stored in dp. The offset variable advances to i exactly when i is a new power of 2,
detected by checking whether offset * 2 == i.

Example: n = 5
    i=1: offset=1,  dp[1] = 1 + dp[0] = 1
    i=2: offset->2, dp[2] = 1 + dp[0] = 1   (2 is a new power of 2)
    i=3: offset=2,  dp[3] = 1 + dp[1] = 2
    i=4: offset->4, dp[4] = 1 + dp[0] = 1   (4 is a new power of 2)
    i=5: offset=4,  dp[5] = 1 + dp[1] = 2
    result: [0, 1, 1, 2, 1, 2]

Time: O(n)
    Single pass from 1 to n; each index filled in O(1)
Space: O(n)
    dp array holds n + 1 entries
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        # dp[i] = bits in i
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            # i is a new power of 2, so the leading-bit position shifts up
            if offset * 2 == i:
                offset = i
            # strip the leading bit; the remaining bits form i - offset, already solved
            dp[i] = 1 + dp[i - offset]
        return dp

'''
O(n log n)
'''
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         res = []
#         for num in range(n + 1):
#             count = 0
#             while num:
#                 count += num % 2
#                 # right shift happens logn times with base 2
#                 num = num >> 1

#             res.append(count)
        
#         return res

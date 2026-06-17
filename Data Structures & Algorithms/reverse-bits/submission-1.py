'''
Time: O(32) = (1)
Space: O(1)
'''
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            # check if the rightmost bit on n is a 1
            bit = n % 2
            # rightshift n
            n = n >> 1
            # move last bit left by one
            res = res << 1
            # add bit to res if it was set on n
            res += bit
        
        return res
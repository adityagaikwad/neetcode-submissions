class Solution:
    def reverseBits(self, n: int) -> int:
        # O(1)
        res = 0

        for i in range(32):
            # check if bit at i'th pos is a 1
            bit = (n >> i) & 1
            # add 2^(31 - i) to the res if the bit was 1
            # i.e reversed order
            res += (bit << (31 - i))
        
        return res

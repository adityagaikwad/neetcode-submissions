'''
At the bit level, addition works using two simple ideas:

XOR (^) gives the sum of two bits without considering carry
AND (&) + left shift determines where a carry is generated
For example (single bit):

0 + 0 → sum = 0, carry = 0
1 + 0 → sum = 1, carry = 0
1 + 1 → sum = 0, carry = 1
By repeating this logic for all bit positions, we can simulate normal addition
exactly as it happens in hardware.

Because integers are stored in fixed-width (32-bit) two's complement form,
we also need to:
1. limit results to 32 bits
2. correctly convert the result back if it represents a negative number

Time and Space: O(1)
'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        # value for -1 in 2's complement format
        # anding with mask will do (* -1)
        mask = 0xFFFFFFFF

        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            cur_bit = a_bit ^ b_bit ^ carry
            carry = (a_bit + b_bit + carry) >= 2
            if cur_bit:
                res = res | (1 << i)

        # max val in hexadecimal format for signed 32 bit num = 0x7FFFFFFF
        # -1 + 0 would get set to 32 1s which python might not know to convert
        # from unsigned 32 to signed 32 bits so we use xor to convert 2^32 to 0
        # then do ~x = -(x + 1) 2's complement to make it -1
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)

        return res
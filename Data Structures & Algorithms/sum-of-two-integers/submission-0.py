class Solution:
    def getSum(self, a: int, b: int) -> int:
        # value for -1 in 2's complement format
        # anding with mask will do (* -1)
        mask = 0xFFFFFFFF
        # max val in hexadecimal format for signed 32 bit num
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)
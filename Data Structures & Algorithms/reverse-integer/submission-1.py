
class Solution:
    def reverse(self, x: int) -> int:
        MIN = -(2**31)
        MAX = 2**31 - 1

        res = 0
        while x:
            # math.fmod performs floating-point modulus and preserves the sign of the dividend (x),
            # which gives the correct last digit for both positive and negative numbers.
            # - 1 % 10  = 9 in python. we want -1 % 10 = -1
            digit = int(math.fmod(x, 10))
            # round towards 0
            x = int(x / 10)

            # if res is going greater than MAX upto second last digit, it may overflow at last digit
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            # if res is going to be less than MIN upto second last digit, it may overflow at last digit
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit

        return res
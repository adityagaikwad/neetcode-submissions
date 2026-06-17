class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        '''
        O(n)
        '''
        # res = 1
        # for i in range(abs(n)):
        #     res *= x
        # return res if n >= 0 else 1 / res

        '''
        O(log n)

        if n = 13 i.e 1101 i.e x^13 = x^8 * x^4 * x^1
        If the curr bit is 1, we multiply by x
        Then square the base for the next bit position
        Then right shift n(power) by 1 to get next bit
        Repeat till power is != 0
        '''
        power = abs(n)
        res = 1

        while power:
            if power & 1:
                res *= x
            
            x *= x
            power = power >> 1
        
        return res if n > 0 else 1/res

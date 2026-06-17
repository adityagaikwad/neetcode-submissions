class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        Time: O(32) = O(1)
        Space: O(1)
        '''
        res = 0

        while n:
            # if n has 1 in last binary digit, we have a 1, count it
            # else 0, no change to res
            res += n % 2

            # we right shift binary bits by 1 to
            # replace prev bit with secondlast from right
            # then we see if that bit was 1 and so on till only
            # 00000 remains i.e n = 0
            n = n >> 1

        return res

        '''
        Alternate approach to count just 1's directly

        Time: O(nums of 1 in n) = O(1)
        Space: O(1)
        '''

        res = 0
        while n:
            # when we & with n - 1 we flip last bit
            # eg. 5 = 0101, 4 = 0100, 3 = 0011
            # 0101 & 0100 = 0100
            # 0100 & 0011 = 0000
            # hence 2 1's counted
            n = n & (n - 1)
            res += 1
        
        return res
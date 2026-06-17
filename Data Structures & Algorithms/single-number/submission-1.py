class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        Hashset O(n) both
        '''
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         seen.remove(num)
        #     else:
        #         seen.add(num)
        # return list(seen)[0]

        '''
        Bit manipulation
            XOR all nums, remaining is non-duplicate val
            1 ^ 1 and 0 ^ 0 = 0
            1 ^ 0 and 0 ^ 1 = 1

            So if we XOR 2 ^ 2 it equals 0. So only the non-dupliate num remains here
            Since 2 = 010. i.e 010 ^ 010 = 000
        Time: O(n)
        Space: O(1)
        '''

        res = nums[0]

        for num in nums[1:]:
            # XOR all nums
            res = num ^ res
        
        return res
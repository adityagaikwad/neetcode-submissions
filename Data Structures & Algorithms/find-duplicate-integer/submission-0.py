class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Hashmap and separate bucket of size n
        are both O(n) space solutions
        '''

        '''
        Negate the number at nums[num - 1] for marking num is visited
        Time: O(n)
        Space: O(1)
        '''

        for num in nums:
            markIdx = abs(num) - 1

            if nums[markIdx] < 0:
                return abs(num)
            
            nums[markIdx] *= -1
        
        return -1
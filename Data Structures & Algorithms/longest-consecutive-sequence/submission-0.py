class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Brute force with set
        '''
        numSet = set(nums)
        ans = 0

        # starting from each num, check for other consecutive
        # numbers which are in the nums arr
        for num in nums:
            streak, curr = 0, num
            while curr in numSet:
                streak += 1
                curr += 1
            
            ans = max(ans, streak)
        
        return ans
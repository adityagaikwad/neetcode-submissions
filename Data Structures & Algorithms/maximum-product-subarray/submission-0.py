class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Time: O(n)
        Space: O(1)
        
        This solution works by tracking both the maximum and minimum product ending at each position
        because a negative number can turn a small minimum into a large maximum. At each step, it updates
        currMax and currMin by considering the current number alone, the product with the previous currMax,
        and with currMin
        '''

        res = nums[0]
        currMin, currMax = 1, 1

        for num in nums:
            temp = currMax * num
            currMax = max(currMax * num, currMin * num, num)
            currMin = min(temp, currMin * num, num)

            res = max(res, currMax)
        
        return res
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Kedane's algorithm (Greedy)

        At each num we check if the sum of currSubarr + num is greater than num
        aka do we continue existing subarr or start a new one? Coz if sum is lower
        starting new from num will give us the bigger sum arr in the future
        
        Time: O(n)
        Space: O(1)
        '''
        if not nums:
            return None

        currSubArray = nums[0]
        maxSubArray = nums[0]

        for num in nums[1:]:
            # if currSubArray is negative, check if we wanna include num
            # (to increase currSubArray) or start a new arr from num
            currSubArray = max(num, currSubArray + num)
            maxSubArray = max(maxSubArray, currSubArray)

        return maxSubArray
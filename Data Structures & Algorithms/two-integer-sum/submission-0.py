class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numPos = {}

        for i, num in enumerate(nums):
            sumDiff = target - num
            if sumDiff in numPos:
                return [numPos[sumDiff], i]
            
            numPos[num] = i
        
        return [-1, -1]

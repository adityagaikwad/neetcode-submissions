class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = {}

        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in numIndex:
                return [numIndex[remaining], i]
            
            numIndex[num] = i
        
        return [-1, -1]

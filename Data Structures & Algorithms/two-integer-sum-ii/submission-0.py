class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1

        while l < r:
            currSum = numbers[l] + numbers[r]
    
            if currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            else:
                return [l + 1, r + 1]

        return []
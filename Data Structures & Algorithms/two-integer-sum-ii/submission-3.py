class Solution:
    '''
    Time: O(n)
    Space: O(1)
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n - 1

        while left < right:
            currSum = numbers[left] + numbers[right]
            if currSum < target:
                left += 1
            elif currSum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        
        return [-1, -1]
             
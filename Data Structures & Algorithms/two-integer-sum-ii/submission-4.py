class Solution:
    '''
    Start with one ptr on leftmost and one on the rightmost
    Then if sum of two nums < target, advance left
    if sum > target, subtract right ptr pos
    if equal, return l + 1, r + 1
    
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
             
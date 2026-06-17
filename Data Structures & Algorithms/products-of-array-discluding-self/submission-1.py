class Solution:
    '''
    Two pass solution
    
    Create two arrs - productLeft and productRight
    output[i] = productLeft[i] * productRight[i]

    Time Complexity: O(n)
    Space Complexity: O(n)

    n = len(nums)
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        productLeft = [1] * n
        productRight = [1] * n

        # calculate productLeft
        for i in range(1, n):
            productLeft[i] = productLeft[i - 1] * nums[i - 1]
        
        # calculate productRight
        # left inclusive, right exclusive
        # productRight[n - 1] = 1
        for i in range(n - 2, -1, -1):
            productRight[i] = productRight[i + 1] * nums[i + 1]
        
        output = [1] * n
        for i in range(n):
            output[i] = productLeft[i] * productRight[i]
        
        return output
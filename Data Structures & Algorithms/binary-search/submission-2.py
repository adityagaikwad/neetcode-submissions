class Solution:
    '''
    Iterative
    '''
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        # <= start and end can point to the same index, and that index might be the target
        while start <= end:
            #  start + end can overflow if both are large integers so do as below
            mid = start + (end - start)//2

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        
        return -1
    
    '''
    Recursive
    '''
    # def binarySearch(self, left: int, right: int, nums: List[int], target: int) -> int:
    #     if left > right:
    #         return -1
        
    #     mid = left + (right - left)//2

    #     if nums[mid] < target:
    #         return self.binarySearch(mid + 1, right, nums, target)
    #     elif nums[mid] > target:
    #         return self.binarySearch(left, mid - 1, nums, target)
    #     else:
    #         return mid

    # def search(self, nums: List[int], target: int) -> int:
    #     return self.binarySearch(0, len(nums) - 1, nums, target)
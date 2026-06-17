class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left)//2
            # complete arr[mid: right + 1] is sorted
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
            
        return nums[left]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        # <= start and end can point to the same index, and that index might be the target
        while start <= end:
            mid = start + (end - start)//2

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        
        return -1
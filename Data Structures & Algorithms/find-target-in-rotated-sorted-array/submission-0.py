class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l)//2

            if nums[mid] == target:
                return mid

            # mid in left of pivot sorted arr
            if nums[l] <= nums[mid]:
                # target outside of sorted arr vals
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    # else, target inside nums[l: mid]
                    r = mid - 1
            
            # mid is in right of pivot sorted arr
            else:
                # target outside of sorted arr vals
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    # else, target inside nums[mid + 1: r + 1]
                    l = mid + 1
        
        return -1
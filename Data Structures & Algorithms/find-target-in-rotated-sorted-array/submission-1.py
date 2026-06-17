'''
Two-pass binary search.

Pass 1 — find the pivot (index of the minimum element) using lower bound search.
The array has two sorted halves, e.g. [3,4,5,6,1,2].
Elements in the right half satisfy nums[i] <= nums[-1]; the pivot is the leftmost such index.

Pass 2 — determine which sorted half the target lives in, then standard binary search.
    - If target is in [nums[pivot], nums[-1]]: search the right half (left = pivot)
    - Otherwise: search the left half (right = pivot - 1)

Example: nums = [3,4,5,6,1,2], target = 1
    Pass 1: pivot = 4  (nums[4] = 1, the minimum)
    Pass 2: target=1 >= nums[4]=1 and <= nums[5]=2 -> search right half [1,2]
            binary search finds index 4.

Time: O(log n), Space: O(1)
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = None
        n = len(nums)

        left, right = 0, n - 1
        # lowerbound binary search to get smallest num pos
        while left < right:
            mid = left + (right - left)//2

            # mid is in right sorted part, can be min too
            # move right to mid
            if nums[mid] <= nums[-1]:
                right = mid
            # else mid > last so its in left sorted part, cannot be min
            # move left to the mid + 1 pos
            else:
                left = mid + 1
        
        # pivot is min idx pos
        pivot = left

        left, right = 0, n - 1
        # check if we need to binary search in left half of sorted arr or right
        if target >= nums[pivot] and target <= nums[right]:
            # search right half including pivot
            left = pivot
        else:
            # search left half excluding min/pivot
            right = pivot - 1
        

        # normal binary search
        while left <= right:
            mid = left + (right - left)//2

            # search right
            if nums[mid] < target:
                left = mid + 1
            # search left
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        
        return -1

'''
One pass log(n) solution

At each pos, check if mid is in left half of sorted arr or right
And then check if target falls between l:mid or mid + 1:r and update
l, r accordingly to narrow arr
'''
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
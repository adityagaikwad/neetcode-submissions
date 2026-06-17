'''
Classic Binary search using l <= r style.

Key observation: in a rotated sorted array, one half is always normally sorted.
Compare nums[m] with nums[l] to determine which half mid falls in:

    Left sorted portion:  nums[l] <= nums[m]  (e.g. [3,4,5,1,2], mid=5)
    -> the drop (and minimum) must be to the right, so l = m + 1

    Right sorted portion: nums[m] < nums[l]   (e.g. [3,4,5,1,2], mid=1)
    -> mid could be the minimum or it's further left, so r = m - 1

Early exit: if nums[l] < nums[r], the current window is fully sorted,
so nums[l] is the local minimum — no need to keep searching.

res tracks the running minimum across all mid values seen.

Example: nums = [3,4,5,6,1,2]
    l=0 r=5: nums[l]=3 > nums[r]=2, not sorted. m=2, nums[m]=5 > nums[l]=3 -> l=3
    l=3 r=5: nums[l]=6 > nums[r]=2, not sorted. m=4, nums[m]=1 < nums[l]=6 -> r=3
    l=3 r=3: nums[l]=6 > nums[r]=6? No, equal -> early exit, res=min(res,6)...
    wait, actually l==r so nums[l]==nums[r], early exit fires, res=min(res,nums[3]=6)
    -> returns min seen so far = 1. Correct.

Time: O(log n), Space: O(1)
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        
        l, r = 0, n - 1
        
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            
            m = l + (r - l)//2
            res = min(res, nums[m])

            # mid is in left sorted portion,
            # min has to be to the right of mid
            # eg. [3 4 (5) 1 2]
            if nums[m] >= nums[l]:
                l = m + 1
            # else, mid is in right sorted portion and
            # we need to search left of it to get min
            else:
                r = m - 1
        
        return res

'''
Lower bound binary search: find the leftmost index where the condition
"nums[i] <= nums[-1]" is True.

In a rotated sorted array the array looks like two sorted halves:
    [left portion: all > nums[-1]] [right portion: all <= nums[-1]]
    e.g. [3, 4, 5, 6, 1, 2]
        F  F  F  F  T  T      <- condition: nums[i] <= nums[-1]

The minimum is exactly the first True, i.e. the start of the right portion.

Lower bound rule:
    - condition True  -> r = mid   (mid is a candidate, don't exclude it)
    - condition False -> l = mid+1 (mid is too far left, exclude it)
    Loop ends when l == r, which is the leftmost True index.

Edge case: array not rotated e.g. [1,2,3,4,5]
    All elements satisfy nums[i] <= nums[-1], so first True is index 0. Correct.

Time: O(log n)
Space: O(1)
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] <= nums[-1]:
                # mid is in the right sorted portion, could be the minimum
                r = mid
            else:
                # mid is in the left sorted portion, minimum is to the right
                l = mid + 1

        return nums[l]
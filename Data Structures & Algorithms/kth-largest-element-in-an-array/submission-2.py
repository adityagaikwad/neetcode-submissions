'''
Min heap

Time: O(nlogk)
Space: O(k)
'''
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         minHeap = []

#         for num in nums:
#             heappush(minHeap, num)

#             if len(minHeap) > k:
#                 heappop(minHeap)
        
#         return minHeap[0]

'''
QuickSelect with partition, recursive

When we have placed the pivot at index len(nums) - k, it means its that num's
final pos. So its n - kth smallest aka kth largest num in the arr. Return it

The k-th largest sits at index len(nums) - k in a sorted ascending array,
stored as requiredPivotPos. Each call to quickSelect(l, r) picks nums[r] as
the pivot and rearranges the window [l, r] so all elements smaller than or
equal to the pivot land left of storeIdx, then places the pivot itself at
storeIdx. If storeIdx equals requiredPivotPos the pivot is the answer;
otherwise only the half containing requiredPivotPos is recursed into, discarding
the other side entirely. This is correct because after partitioning,
the pivot is at its final sorted position regardless of the order
within each half.

Time: O(n) average
    Expected total work: n + n/2 + n/4 + ... = 2n since only one side is recursed into
    O(n²) worst case when pivot always lands at the edge (mitigated with random pivot)
Space: O(log n) average
    Call stack depth equals the number of halvings before landing on requiredPivotPos
    O(n) worst case on maximally skewed partitions
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # index the k-th largest occupies in a fully sorted ascending array
        requiredPivotPos = len(nums) - k

        def quickSelect(l, r):
            # l, r: inclusive bounds of the subarray currently being partitioned
            # pivot: value of nums[r], the rightmost element chosen as the partition anchor
            # storeIdx: write pointer tracking where the next element <= pivot should be placed
            pivot, storeIdx = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[storeIdx] = nums[storeIdx], nums[i]
                    storeIdx += 1  # advance write pointer after placing an element on the left side

            # pivot moves from nums[r] to storeIdx; everything left is <= pivot, right is > pivot
            nums[r], nums[storeIdx] = nums[storeIdx], nums[r]

            if storeIdx > requiredPivotPos:
                return quickSelect(l, storeIdx - 1)
            elif storeIdx < requiredPivotPos:
                return quickSelect(storeIdx + 1, r)
            else:
                return nums[storeIdx]  # storeIdx is now the final sorted position of the answer

        return quickSelect(0, len(nums) - 1)

'''
Quick select iterative

Time:
    O(n) avg
    O(n ^ 2) worst when sorted either ascending or descending
Space:
    O(1) extra space
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k  # k-th largest sits at this index in ascending sorted order
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = nums[right]
            storeIdx = left

            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[storeIdx] = nums[storeIdx], nums[i]
                    storeIdx += 1

            nums[right], nums[storeIdx] = nums[storeIdx], nums[right]

            if storeIdx == target:
                break
            elif storeIdx < target:
                left = storeIdx + 1
            else:
                right = storeIdx - 1

        return nums[target]
from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Min heap
        Time: O(nlogk)
        Space: O(k)
        '''
        # minHeap = []

        # for num in nums:
        #     heappush(minHeap, num)

        #     if len(minHeap) > k:
        #         heappop(minHeap)
        
        # return minHeap[0]

        '''
        Quick select recursive

        Time:
            Average: O(n) -> n + n/2 + n/4 + ... = 2n = O(n)
            Worst: O(n^2) -> n + n-1 + n-2 + ... = n(n+1)/2 = O(n^2)
        Space: O(n) stack size
        '''
        # 0 indexed
        # n = 5, k = 2 - > 0 1 2 3 4 (we need to return 3) = 5 - 2
        requiredPivotPos = len(nums) - k

        def quickSelect(l, r):
            pivot, pos = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[pos] = nums[pos], nums[i]
                    pos += 1

            nums[r], nums[pos] = nums[pos], nums[r]

            if pos > requiredPivotPos:
                return quickSelect(l, pos - 1)
            elif pos < requiredPivotPos:
                return quickSelect(pos + 1, r)
            else:
                return nums[pos]

        return quickSelect(0, len(nums) - 1)

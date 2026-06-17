class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        Hashmap and separate bucket of size n
        are both O(n) space solutions
        '''

        '''
        Negate the number at nums[num - 1] for marking num is visited
        Time: O(n)
        Space: O(1)
        '''
        for num in nums:
            markIdx = abs(num) - 1

            if nums[markIdx] < 0:
                return abs(num)
            
            nums[markIdx] *= -1
        
        return -1

        '''
        Hard question:

        Floyd's algorithm linked list approach to find duplicate without
        modifying original arr and still being O(n) time and O(1) space.

        treat the array as a linked list where each index i
        points to nums[i] as its "next" node. Starting at index 0:

        0 -> nums[0] -> nums[nums[0]] -> ...

        Example: nums = [1, 3, 4, 2, 2]

        Index:  0  1  2  3  4
        Value:  1  3  4  2  2

        Each index points to the value at that index as its "next node":

        0 -> nums[0] = 1
        1 -> nums[1] = 3
        2 -> nums[2] = 4
        3 -> nums[3] = 2
        4 -> nums[4] = 2

        Traversal starting from index 0:

        Traversal: 0 -> 1 -> 3 -> 2 -> 4 -> 2 -> 4 -> 2 ...
                                    ^         |
                                    |_________|
                                    cycle entrance = 2 (the duplicate)

        Both index 3 and index 4 hold the value 2, so two different nodes point
        to node 2 as their next. That convergence is what creates the cycle, and
        that point is the duplicate.

        Values are in [1, n] so nothing ever points back to index 0. This gives
        a "rho" shape (a tail leading into a cycle) which Floyd's algorithm requires.

        A cycle is guaranteed because there are n + 1 values all in [1, n], so
        at least one value must repeat.

        Phase 1 - find detection point:
            Move slow by 1 step and fast by 2 steps until they meet somewhere
            inside the cycle. This meeting point is NOT the cycle entrance.

        Phase 2 - find cycle entrance (= duplicate):
            Reset slow2 to index 0. Advance slow (from detection point) and slow2
            (from start) one step at a time. Where they meet is the cycle entrance,
            which is the duplicate number.
        '''
        # slow, fast = 0, 0

        # # find the detection point of the cycle using slow and fast
        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        
        #     if slow == fast:
        #         break
        
        # # move slow2 and slow (which is at detection point) together by 1
        # # till they match, this is start of the cycle and the duplicate num
        # slow2 = 0
        # while True:
        #     slow = nums[slow]
        #     slow2 = nums[slow2]

        #     if slow == slow2:
        #         return slow

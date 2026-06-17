'''
Time: O(n * 2^n)
    n for copying arr, 2^n coz each element would be either chosen or not chosen
    2^n subsets total if no duplicate nums

Space: O(n)
    call stack can go n levels deep max
    currArr size can also go upto n max
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        # sort the input array to handle duplicate subsets
        nums.sort()

        def backtrack(start, currArr):
            res.append(currArr[:])

            for i in range(start, n):
                # skip duplicates starts to avoid duplicate subsets
                if i > start and nums[i] == nums[i-1]:
                    continue

                backtrack(i + 1, currArr + [nums[i]])

        backtrack(0, [])
        return res
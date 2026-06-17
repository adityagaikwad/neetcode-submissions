class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subs, nums):
            output.append(list(subs))  # add the current subset to the output list
            for i in range(start, len(nums)):
                # skip duplicates
                if i > start and nums[i] == nums[i-1]:
                    continue
                subs.append(nums[i])   # add the current element to the current subset
                backtrack(i + 1, subs, nums)  # recursively call the backtracking function with the updated subset and index
                subs.pop() # remove the current element from the subset before returning

        output = []
        nums.sort()  # sort the input array to handle duplicates
        backtrack(0, [], nums)  # call the backtracking function with an empty subset and starting index of 0
        return output
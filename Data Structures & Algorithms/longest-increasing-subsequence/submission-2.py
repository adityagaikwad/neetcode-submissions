'''
Time: O(n^2)
    For each i, there can be n prevNums
Space: O(n^2)
    For each i, there can be n prevNums
    Memo will be n^2
'''
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)

#         memo = {}
#         def dfs(i, prevNum):
#             if i == n:
#                 return 0

#             if (i, prevNum) in memo:
#                 return memo[(i, prevNum)]
            
#             # do not include curr num
#             res = dfs(i + 1, prevNum)
            
#             # include curr num
#             if nums[i] > prevNum:
#                 res = max(res, 1 + dfs(i + 1, nums[i]))

#             memo[(i, prevNum)] = res
#             return res

        # return dfs(0, float("-inf"))

'''
Binary search on patience-sort subsequence

We maintain `subsequence` where index i holds the smallest possible tail for
any increasing subsequence of length i+1 seen so far. For each num, if it
exceeds the current tail we append it, growing the LIS length by one.
Otherwise, we binary search for the first element >= num and replace it,
which shrinks the tail at that length without changing the overall length.

The final `subsequence` may not be a valid subsequence of the input, but
its length equals the LIS length. Length only increases when num > subsequence[-1],
meaning a strictly longer increasing subsequence was genuinely found.

Time: O(n log n)
    Each of the n elements triggers at most one binary search over at most n elements
Space: O(n)
    subsequence grows to at most n elements when the input is strictly increasing
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def binary_search(arr, target):
            l = 0
            r = len(arr) - 1

            while l <= r:
                m = l + (r - l)//2

                if arr[m] == target:
                    return m
                elif arr[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            # when target is absent, l lands on the first index where arr[l] > target
            return l

        # build subsequence of the smallest nums as we go across the arr
        subsequence = []

        for num in nums:
            if not subsequence or num > subsequence[-1]:
                subsequence.append(num)
            else:
                # replacing with a smaller value keeps the tail minimal at this length,
                # making room for more future extensions
                insertion_idx = binary_search(subsequence, num)
                subsequence[insertion_idx] = num

        return len(subsequence)
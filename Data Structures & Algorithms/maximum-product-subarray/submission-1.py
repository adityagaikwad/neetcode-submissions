'''
Kadane's variant tracking current min and max product

At each position, the maximum product subarray ending here is one of:
extending the previous max subarray (currMax * num), extending the previous
min subarray (currMin * num, when num is negative this flips to the largest),
or starting a new subarray at num alone. Tracking both extremes is necessary
because a single negative number can turn the smallest running product into
the largest at the next step.

currMax = max product of any subarray ending at the current element
currMin = min product of any subarray ending at the current element

Time: O(n)
    Single pass over the array, constant work per element
Space: O(1)
    Only a fixed number of variables regardless of input size
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin, currMax = 1, 1

        for num in nums:
            # save old currMax * num before overwriting currMax; currMin needs it
            temp = currMax * num
            currMax = max(currMax * num, currMin * num, num)
            currMin = min(temp, currMin * num, num)

            res = max(res, currMax)

        return res
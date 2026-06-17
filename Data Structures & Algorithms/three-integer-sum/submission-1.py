class Solution:
    '''
    Sort the array, then fix one number nums[i] and use two pointers
    to find two other numbers whose sum is -nums[i] (sorted 2sum)
    Since the array is sorted, move left/right based on whether the sum
    is too small or too large, while skipping duplicates.

    Time: O(n^2)
    Space: O(1)
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sorting lets us use two pointers and easily detect duplicates.
        nums.sort()
        n = len(nums)
        res = []

        # nums[i] is the first number in the triplet.
        # We need at least two numbers after i, so stop at n - 2.
        for i in range(n - 2):

            # If this first number was already processed, skip it.
            # Otherwise, we could generate the same triplet again.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Since the array is sorted, if nums[i] is positive,
            # all numbers after it are also positive, so sum cannot be 0.
            if nums[i] > 0:
                break

            # We now need two numbers that add up to -nums[i].
            target = -nums[i]

            # Search for the remaining two numbers between l and r.
            l = i + 1
            r = n - 1

            while l < r:
                currSum = nums[l] + nums[r]

                # Sum is too small, so move left pointer right
                # to increase the sum.
                if currSum < target:
                    l += 1

                # Sum is too large, so move right pointer left
                # to decrease the sum.
                elif currSum > target:
                    r -= 1

                # Found three numbers whose total sum is 0.
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    # Move both pointers because the current pair
                    # has already been used in a valid triplet.
                    l += 1
                    r -= 1

                    # Skip duplicate left values.
                    # Compare with l - 1 because that is the value
                    # we just used in the triplet.
                    # Once l >= r, there is no valid pair left to check.
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicate right values.
                    # Compare with r + 1 because that is the value
                    # we just used in the triplet.
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res
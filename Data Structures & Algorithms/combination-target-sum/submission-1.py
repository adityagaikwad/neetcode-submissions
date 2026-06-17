'''
Backtracking

We build combinations incrementally, tracking the remaining sum needed at each
call. Passing i (not i + 1) to the recursive call allows the same element to be
reused, which is the key difference from standard subset generation. Passing i as
the start index also ensures we never revisit earlier elements, so each unique
multiset is generated exactly once regardless of the order elements appear in nums.
Pruning on remaining < 0 cuts branches that have already overshot the target.

Time: O(n^(t/m))
    Max time would be spent on subtracting the smallest element t/m times.
    Worst case is doing this n times.

    The tree has depth at most t/m (each call reduces remaining by at least m);
    at each level up to n branches are explored

    t = target
    m = min(nums)

Space: O(t/m)
    Call stack depth is bounded by target divided by the smallest element,
    since every recursive call subtracts at least min(nums) from remaining
'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        # allows early exit/break in for loop
        nums.sort()

        def backtrack(start, currArr, remaining):
            # no point in recursing further
            if remaining < 0:
                return

            if remaining == 0:
                res.append(currArr[:])
                return
            

            for i in range(start, n):
                # no point in backtracking, all further nums are greater
                if nums[i] > remaining:
                    break

                # pass i and not i + 1 coz same num can be used twice
                backtrack(i, currArr + [nums[i]], remaining - nums[i])
        
        backtrack(0, [], target)

        return res
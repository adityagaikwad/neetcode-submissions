'''
Backtracking

At each call, the current list is a valid subset, so it is recorded immediately.
We then extend it by appending each element from startFrom onward, recurse to
explore all supersets of that choice, then remove the element to restore the list
for the next branch. Because startFrom always advances past the last chosen index,
no element is ever picked twice in the same subset and no subset is generated twice.

Time: O(n * 2^n)
    There are 2^n subsets total; copying each one costs O(n) in the worst case,
    giving n * 2^n total work across all calls
Space: O(n)
    The call stack goes at most n levels deep, one level per element chosen;
    the output list itself is excluded from auxiliary space
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        ans = []

        def backtrack(startFrom, currList):
            ans.append(currList[:])

            for i in range(startFrom, n):
                num = nums[i]
                currList.append(num)
                # start next iteration from i + 1
                # since we added i already to currList
                backtrack(i + 1, currList)
                # to allow for subset starting from nums[i + 1]
                # eg [1,2,3] -> subset [2], [2, 3]
                currList.pop()

        backtrack(0, [])
        return ans
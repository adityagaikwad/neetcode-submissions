class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(remainingSum, currList, startFrom):
            if remainingSum < 0:
                return

            if remainingSum == 0:
                ans.append(currList[:])
                return
            
            for i in range(startFrom, n):
                num = nums[i]
                if num > remainingSum:
                    continue

                currList.append(num)
                backtrack(remainingSum - num, currList, i)
                currList.pop()

        backtrack(target, [], 0)
        return ans
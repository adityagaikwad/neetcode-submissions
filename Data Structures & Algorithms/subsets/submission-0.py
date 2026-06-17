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
                currList.pop()
        
        backtrack(0, [])
        return ans
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def backtrack(currList):
            if len(currList) == n:
                ans.append(currList[:])
                return
            
            for num in nums:
                if num not in currList:
                    currList.append(num)
                    backtrack(currList)
                    currList.pop()
        
        backtrack([])
        return ans
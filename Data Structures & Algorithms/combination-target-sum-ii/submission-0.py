class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []

        def backtrack(startFrom, remainingSum, currList):
            if startFrom > n or remainingSum < 0:
                return
            
            if remainingSum == 0:
                ans.append(currList[:])
                return

            for i in range(startFrom, n):
                # skip over duplicates if it has already been processed
                if i > startFrom and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remainingSum:
                    break

                currList.append(candidates[i])
                backtrack(i + 1, remainingSum - candidates[i], currList)
                currList.pop()
        
        candidates.sort()
        backtrack(0, target, [])

        return ans
'''
Backtracking with duplicate skip

Sort candidates so duplicates sit adjacently and so we can break early
when a candidate already exceeds the remaining sum. At each recursive
level, iterate over candidates from `start` onward: append a candidate,
recurse with `i + 1` (each element used at most once) and the reduced
remaining, then pop to undo.

The duplicate-skip guard `i > start and candidates[i] == candidates[i-1]`
prevents picking the same value twice at the same depth level. Using
`i > start` instead of `i > 0` is the key distinction: within a single
call we must allow the first occurrence, but any later sibling with the
same value would produce an identical subtree, so we skip it.

Time: O(2^n)
    Each candidate is either included or excluded; worst case explores all subsets
Space: O(n)
    Call stack depth and currArr length are both bounded by the number of candidates
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        
        res = []
        # to skip over duplicates of same num as arr start and overall
        # avoid duplicate combinations from them
        candidates.sort()

        def backtrack(start, remaining, currArr):
            if remaining < 0 or start > n:
                return
            
            if remaining == 0:
                res.append(currArr[:])
                return
            
            for i in range(start, n):
                # if we already started a new arr from i at i = start
                # skip other duplicate combinations starting from candidates[i]
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > remaining:
                    break
                
                backtrack(i + 1, remaining - candidates[i], currArr + [candidates[i]])
        
        backtrack(0, target, [])

        return res




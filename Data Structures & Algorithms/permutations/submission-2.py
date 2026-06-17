'''
Time Complexity: O(n * n!)
    Total permutations possible = n!, O(n) time to copy over each arr

Space: O(n)
    Recursion call stack goes upto O(n)
    Same with currArr len

'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        n = len(nums)
        visited = [False] * n

        def backtrack(currArr):
            if len(currArr) == n:
                res.append(currArr[:])
                return
            
            for i, num in enumerate(nums):
                if not visited[i]:
                    currArr.append(num)
                    visited[i] = True

                    backtrack(currArr)
                    currArr.pop()
                    visited[i] = False
        
        backtrack([])

        return res

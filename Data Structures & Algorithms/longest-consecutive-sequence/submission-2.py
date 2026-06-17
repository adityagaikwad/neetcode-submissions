class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        uniqueNums = set(nums)

        maxLen = 1
        marked = set()
        for num in uniqueNums:
            if num not in marked and (num - 1) not in uniqueNums:
                nextNum = num + 1
                currLen = 1
                while nextNum in uniqueNums:
                    marked.add(nextNum)
                    currLen += 1
                    maxLen = max(maxLen, currLen)
                    nextNum += 1
        
        return maxLen
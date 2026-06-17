class Solution:
    '''
    We convert it to a set and to avoid duplicate counting from the middle 
    of a sequence for eg if set is 12345 to avoid double counting from 3 to 45
    we check if (num-1) is in the set, so we only start from first num in the sequence

    Count lens of all such sequences, we go through each num only once so O(n)

    Time: O(n)
    Space: O(n) for uniqueNums
    '''
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)

        maxLen = 0
        for num in uniqueNums:
            # Only start counting from the beginning of a sequence
            if (num - 1) not in uniqueNums:
                nextNum = num + 1
                currLen = 1

                while nextNum in uniqueNums:
                    currLen += 1
                    nextNum += 1
                
                maxLen = max(maxLen, currLen)

        return maxLen
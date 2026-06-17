'''
backtrack starting from (startFrom=0, currPalindromes=[])
if startFrom = n, found a valid substring arr

Else iterate end var from startFrom to n and check if [startFrom: end + 1] (end inclusive)
is a palindrome, if yes, add to currPalindromes and continue checking backtrack(end + 1, currPalindromes)

IMP: then also pop curr palindrome to check for start to another end

Time complexity: O(n* 2^n)
    isPalindrome takes n time
    2^n total partitions since 2 options for each char
    Start new partition or continue substring

Space: O(n) extra space for part
       O(n * 2^n) for res. 2^n options, each of size n
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def backtrack(startFrom, currPalindromes):
            if startFrom == n:
                # if we successfully found all partitions to be palindromes
                # startFrom would equal len(s)
                res.append(currPalindromes.copy())
                return
            
            for end in range(startFrom, n):
                if self.isPalindrome(s, startFrom, end):
                    # inclusive of startFrom and end
                    currPalindromes.append(s[startFrom: end + 1])
                    # find if chars starting from end + 1 of s are also
                    # valid palindromes
                    backtrack(end + 1, currPalindromes)
                    # remove curr palindrome and explore other possibilities
                    currPalindromes.pop()

        backtrack(0, [])
        return res
    
    def isPalindrome(self, s, l, r):
        # since we want to check for palindromes
        # l = r is always palindrome, no need to check
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
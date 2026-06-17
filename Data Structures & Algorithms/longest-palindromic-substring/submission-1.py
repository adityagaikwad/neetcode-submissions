'''
Time: O(n^2)
Space: O(1)
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # left and right chars are not equal so return just one before them
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd length palindromes
            palindrome = expandAroundCenter(i, i)
            if len(palindrome) > len(longest):
                longest = palindrome
            # Even length palindromes
            palindrome = expandAroundCenter(i, i + 1)
            if len(palindrome) > len(longest):
                longest = palindrome
        return longest

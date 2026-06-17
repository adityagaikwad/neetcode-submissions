'''
Time: O(n^2)
      for loop and then expand can be n^2 worst case
Space: O(1)
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandAroundCenter(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        count = 0
        for i in range(len(s)):
            # Odd length palindromes (centered at a single character)
            count += expandAroundCenter(i, i)
            # Even length palindromes (centered between two characters)
            count += expandAroundCenter(i, i + 1)

        return count
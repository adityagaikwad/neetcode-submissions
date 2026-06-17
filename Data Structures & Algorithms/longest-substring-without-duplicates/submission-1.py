class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastPosOfChar = defaultdict(int)

        l = 0
        maxLen = 0
        for r in range(len(s)):
            if s[r] in lastPosOfChar and lastPosOfChar[s[r]] >= l:
                l = lastPosOfChar[s[r]] + 1  # Move left pointer past the last occurrence

            maxLen = max(maxLen, r - l + 1)  # Update the max length
            lastPosOfChar[s[r]] = r  # Update the last seen position of character

        return maxLen


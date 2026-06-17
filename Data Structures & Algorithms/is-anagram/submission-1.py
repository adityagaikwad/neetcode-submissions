from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)

        if sLen != tLen:
            return False

        sCounter = defaultdict(int)
        tCounter = defaultdict(int)

        for i in range(sLen):
            sCounter[s[i]] += 1
            tCounter[t[i]] += 1
        
        return sCounter == tCounter
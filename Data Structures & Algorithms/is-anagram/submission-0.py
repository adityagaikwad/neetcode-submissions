from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        N1, N2 = len(s), len(t)

        if N1 != N2:
            return False

        counter1 = defaultdict(int)
        counter2 = defaultdict(int)

        for i in range(N1):
            counter1[s[i]] += 1
            counter2[t[i]] += 1
        
        return counter1 == counter2
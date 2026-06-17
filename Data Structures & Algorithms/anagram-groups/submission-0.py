from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sameCharLists = defaultdict(list)

        for string in strs:
            sameCharLists[''.join(sorted(string))].append(string)

        return sameCharLists.values()
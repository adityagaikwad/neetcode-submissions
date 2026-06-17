from collections import defaultdict

class Solution:
    '''
    Sorting solution

    n = len(strs)
    m = max(len of strs)

    Time Complexity: O(n * mlogm)

    Space Complexity: O(n*m)
    '''
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     sameChars = defaultdict(list)

    #     for string in strs:
    #         sameChars[str((sorted(string)))].append(string)

    #     return list(sameChars.values())

    '''
    Hashset solution
        Have the key for sameChars be 26 char array's tuple, we add by 1 for each
        char which exists in a string (do not set to 1, duplicate chars may exist)

    n = len(strs)
    m = max(len of strs)

    Time Complexity: O(n * m)

    Space Complexity: O(n * m)
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sameChars = defaultdict(list)

        for string in strs:
            hashKey = [0]*26
            for ch in string:
                hashKey[ord(ch) - ord("a")] += 1
            
            sameChars[tuple(hashKey)].append(string)
        
        return list(sameChars.values())






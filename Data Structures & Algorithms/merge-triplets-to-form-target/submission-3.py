'''
Iterate over all triplets, if any num in triplet t - t[i] > target[i] then skip
this triplet, when merging it will not give us target

For other triplets, check if any num in them matches corresponding triplet, add
idxs of match found (from 1,2,3 pos) to a set.

Return set len == 3 as in all 3 pos had a match found in triplets arr

Time: O(n)
Space: O(1)
        set will be max of size 3
'''
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            # if any num in current triplet is > target val
            # it cannot be used to merge, so skip it
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            # check if any of the 3 elements match the one in target
            # add to good list, if we were able to find all 3, return true
            # else return false
            for i in range(len(t)):
                if t[i] == target[i]:
                    good.add(i)
        
        return len(good) == 3
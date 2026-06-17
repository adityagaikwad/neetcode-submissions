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
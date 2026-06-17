class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Time complexity: O(n*logm)
            m is the max bananas in piles arr
            n is len of piles
        Space complexity: O(1)
        '''
        minK = 1
        res = maxK = max(piles)

        while minK <= maxK:
            k = (minK + maxK) // 2

            totalTimeReq = 0
            for bananas in piles:
                totalTimeReq += math.ceil(bananas/k)
            
            if totalTimeReq <= h:
                res = k
                maxK = k - 1
            else:
                minK = k + 1
        
        return res
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        Time: O(n)
            n is len of s
        Space: O(m)
            m in unique chars in s
        '''
        if not s:
            return []

        lastIndexOfChar = {}

        for i, c in enumerate(s):
            lastIndexOfChar[c] = i
        
        res = []
        size = 0
        end = 0
        for i, c in enumerate(s):
            size += 1
            # keep pushing end if the last entry of a char is
            # further than current end
            if lastIndexOfChar[c] > end:
                end = lastIndexOfChar[c]
            
            # which means all chars in curr substring are
            # not seen beyond idx = end
            if i == end:
                res.append(size)
                size = 0
        
        return res
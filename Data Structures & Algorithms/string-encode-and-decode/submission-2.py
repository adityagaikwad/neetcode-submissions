class Solution:
    '''
    Encode by adding (str len + # + str) to encodedString
    Decode by iterating encodedString till we encounter # to get len of str
    then iterate upto len to get str and repeat

    Time Complexity: O(m)
    Space Complexity: O(m + n)
        Encoded string size is m + n coz we added n new chars

    m = sum of len of all strs
    n = num of strs
    '''
    def encode(self, strs: List[str]) -> str:
        encodedStr = ""

        for string in strs:
            encodedStr += str(len(string)) + "#" + string
        
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedStrs = []

        n = len(s)
        i = 0
        while i < n:
            numStr = ""
            while s[i] != "#":
                numStr += s[i]
                i += 1
            
            strLen = int(numStr)
            
            # move pointer from # to start of string
            i += 1
            
            newStr = ""
            j = 0
            while j < strLen:
                newStr += s[i]
                i += 1
                j += 1
            
            decodedStrs.append(newStr)
        
        return decodedStrs

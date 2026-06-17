class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        n = len(s)

        def dfs(startFrom):
            if startFrom == n:
                # if we successfully found all partitions to be palindromes
                # startFrom would equal len(s)
                res.append(part.copy())
                return
            
            for end in range(startFrom, n):
                if self.isPalindrome(s, startFrom, end):
                    # inclusive of startFrom and end
                    part.append(s[startFrom: end + 1])
                    # find if chars starting from end + 1 of s are also
                    # valid palindromes
                    dfs(end + 1)
                    # remove curr palindrome and explore other possibilities
                    part.pop()
        
        dfs(0)
        return res
    
    def isPalindrome(self, s, l, r):
        # since we want to check for palindromes
        # l = r is always palindrome, no need to check
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
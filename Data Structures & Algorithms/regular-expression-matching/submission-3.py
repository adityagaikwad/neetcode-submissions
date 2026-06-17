class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        Time: O(m * n)
        Space: O(m * n)
        '''
        n1 = len(s)
        n2 = len(p)

        memo = {}
        def dfs(i, j):
            # If both string and pattern are exhausted
            if j == n2:
                return i == n1

            if (i, j) in memo:
                return memo[(i, j)]

            # Check if current characters match
            match = i < n1 and (s[i] == p[j] or p[j] == ".")

            # If next pattern char is '*', we have two options:
            # 1. Skip 'char*' → dfs(i, j+2)
            #    eg. s = "aaab", p = "a*b". i is at "b" and j is at "a"
            #    So we want to skip "a*" and try comparing i at "b" with j at "b"
            # 2. If current matches, use '*' → dfs(i+1, j) and see if future i + 1's match current j
            if (j + 1) < n2 and p[j + 1] == "*":
                memo[(i, j)] = match and dfs(i + 1, j) or dfs(i, j + 2)
                # return right here since no need to explore other paths
                return memo[(i, j)]

            # Normal case: just move ahead if characters match
            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                # return right here since no need to explore other paths
                return memo[(i, j)]

            # no match for any pattern, return False
            memo[(i, j)] = False
            return False

        return dfs(0, 0)
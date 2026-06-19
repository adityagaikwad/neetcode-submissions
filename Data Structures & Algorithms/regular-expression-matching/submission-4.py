'''
Top-down DFS with memoization

At each (i, j) there are two structurally distinct pattern situations:
- p[j+1] == '*': skip the char* pair entirely (zero uses) or consume one char
  from s and stay at j (one or more uses), whichever path succeeds
- otherwise: s[i] and p[j] must match directly, then both pointers advance

dfs(i, j) = whether s[i:] matches p[j:]

Time: O(m * n)
    m * n unique (i, j) states, each computed once via memoization
Space: O(m * n)
    memo table stores one boolean per (i, j) pair; call stack is O(m + n)
    but dominated by the table
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1 = len(s)
        n2 = len(p)

        memo = {}
        def dfs(i, j):
            if j == n2:
                return i == n1

            if (i, j) in memo:
                return memo[(i, j)]

            # i < n1 guard needed: j can still advance past exhausted s via '*' skips
            match = i < n1 and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < n2 and p[j + 1] == "*":
                # 1. skip char* entirely (zero uses): dfs(i, j+2), always valid
                # 2. consume one char from s (one use): dfs(i+1, j), only valid if match;
                #    stay at j so '*' remains active for further chars
                memo[(i, j)] = match and dfs(i + 1, j) or dfs(i, j + 2)
                return memo[(i, j)]

            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]

            memo[(i, j)] = False
            return False

        return dfs(0, 0)
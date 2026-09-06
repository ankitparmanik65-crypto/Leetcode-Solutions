class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Memoization
        m, n = len(s), len(t)
        memo = {}
        
        def dfs(i, j):
            if j == n:
                return 1
            if i == m:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            if s[i] == t[j]:
                result = dfs(i+1, j+1) + dfs(i+1, j)
            else:
                result = dfs(i+1, j)
            
            memo[(i, j)] = result
            return result
        
        return dfs(0, 0)       
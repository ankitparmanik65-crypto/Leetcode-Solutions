class Solution:
    def climbStairs(self, n: int) -> int:
        '''#simple Recursion
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)'''
        #Memoized Recursion
        memo = {}

        def helper(i):
            if i <= 2:
                return i

            if i in memo:
                return memo[i]

            memo[i] = helper(i - 1) + helper(i - 2)
            return memo[i]

        return helper(n)
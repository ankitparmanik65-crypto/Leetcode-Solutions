class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans = 1

        while l <= r:
            mid = (l + r) // 2
            midSquare = mid * mid

            if midSquare > x:
                r = mid - 1 #too big, search smaller
            else:
                ans = mid #valid candidate, try for a bigger one
                l = mid + 1

        return ans
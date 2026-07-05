class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        original = num
        while num > 0:
            digit = num % 10
            if original % digit == 0:
                ans += 1
            num //= 10        
        return ans
        
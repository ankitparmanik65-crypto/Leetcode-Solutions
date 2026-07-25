class Solution:
    def maxProduct(self, n: int) -> int:
        top1 = 0
        top2 = 0
        while n > 0:
            digits = n % 10
            n //= 10
            if digits >= top1:
                top1, top2 = digits, top1
            elif digits > top2:
                top2 = digits
        return top1 * top2
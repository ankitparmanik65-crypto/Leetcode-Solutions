class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Base cases
        if n <= 0:
            return False
        if n == 1:
            return True   
        if n % 3 != 0:
            return False  
        
        # Recursive case
        return self.isPowerOfThree(n // 3)  
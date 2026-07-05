class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #Base case 1
        if n <= 0:
            return False
        #Base case 2
        if n == 1:
            return True
        #Base case 3
        if n % 2 != 0:
            return False

        # Recursive case 
        return self.isPowerOfTwo(n // 2)


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        #in one line 
        #return n

        #Using loop & Euclidean Algorithm
        evenSum = 0
        oddSum = 0

        for i in range(1, n + 1):
            evenSum += 2 * i
            oddSum += 2 * i - 1

        while oddSum != 0:
            rem = evenSum % oddSum
            evenSum = oddSum
            oddSum = rem

        return evenSum
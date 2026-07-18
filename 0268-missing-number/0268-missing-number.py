class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Sum Formula (Gauss's formula) 
        n = len(nums)
        expectedSum = n * (n + 1) // 2
        actualSum = sum(nums)

        return expectedSum - actualSum
        
        #XOR trick
        '''n = len(nums)
        result = n
        for i in range(n):
            result ^= i ^ nums[i]

        return result'''
        
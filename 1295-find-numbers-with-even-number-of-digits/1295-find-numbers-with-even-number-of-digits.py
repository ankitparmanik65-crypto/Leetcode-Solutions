class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        '''#Using string Conversion
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count'''
        
        #Using math (no string conversion)
        count = 0
        for num in nums:
            digits = 0
            n = num
            while n != 0:
                n //= 10
                digits += 1
            if digits % 2 == 0:
                count += 1
        return count
        
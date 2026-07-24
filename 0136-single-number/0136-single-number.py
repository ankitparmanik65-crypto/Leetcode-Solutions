class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #XOR
        '''
        result = 0

        for num in nums:
            result ^= num

        return result
        '''
        #Using set
        seen = set()

        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)

        return seen.pop()


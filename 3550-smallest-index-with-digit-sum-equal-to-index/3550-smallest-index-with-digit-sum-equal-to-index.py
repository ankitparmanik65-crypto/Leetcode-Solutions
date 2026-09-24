class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i, x in enumerate(nums):
            digit_sum = 0

            while x:
                digit_sum += x % 10
                x //= 10

            if digit_sum == i:
                return i

        return -1

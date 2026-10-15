class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0

        for start in range(n):
            distinct = set()

            for end in range(start, n):
                distinct.add(nums[end])
                count = len(distinct)
                total += count * count

        return total
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)

        n = len(nums)
        mid = n // 2

        negative_sum = sum(x * x for x in nums[:mid])
        positive_sum = sum(x * x for x in nums[mid:])

        return positive_sum - negative_sum
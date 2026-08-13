class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # One Pass
        min_value = nums[0]
        ans = -1

        for i in range(1, len(nums)):
            if nums[i] > min_value:
                ans = max(ans, nums[i] - min_value)
            else:
                min_value = nums[i]

        return ans        
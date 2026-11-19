class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # Sorting + Greedy
        nums.sort()

        n = len(nums)

        option1 = nums[n - 1] - nums[2]
        option2 = nums[n - 2] - nums[1]
        option3 = nums[n - 3] - nums[0]

        return min(option1, option2, option3)

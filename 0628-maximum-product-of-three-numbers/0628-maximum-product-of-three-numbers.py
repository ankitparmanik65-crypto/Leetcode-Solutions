class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        product1 = nums[n - 1] * nums[n - 2] * nums[n - 3] #three largest
        product2 = nums[0] * nums[1] * nums[n - 1]#two smallest & largest

        return max(product1, product2)
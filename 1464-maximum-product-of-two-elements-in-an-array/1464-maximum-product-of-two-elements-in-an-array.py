class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #using Sorting 
        # nums.sort()
        # n = len(nums)
        # return (nums[n - 1] - 1) * (nums[n - 2] - 1)

        #using single pass
        top1 = top2 = 0   # top1 = largest, top2 = second largest

        for num in nums:
            if num > top1:
                top2 = top1
                top1 = num
            elif num > top2:
                top2 = num

        return (top1 - 1) * (top2 - 1)
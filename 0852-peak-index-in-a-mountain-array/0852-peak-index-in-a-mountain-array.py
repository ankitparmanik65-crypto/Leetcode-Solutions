class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1 #climbing up, peak is to the right
            else:
                r = mid #descending, peak is mid or to the left

        return l # l == r == peak index
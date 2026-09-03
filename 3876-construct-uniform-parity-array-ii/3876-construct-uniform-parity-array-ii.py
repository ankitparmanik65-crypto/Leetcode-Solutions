class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # Brain Teaser
        mn = float('inf')

        for x in nums1:
            if x % 2 == 1:
                mn = min(mn, x)

        for x in nums1:
            if x % 2 == 0 and mn != float('inf') and x < mn:
                return False

        return True        
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Solution in one line
        # return list(set(nums1) & set(nums2))

        set1=set(nums1)
        set2=set(nums2)
        ans=set1.intersection(set2)
        return list(ans)


        
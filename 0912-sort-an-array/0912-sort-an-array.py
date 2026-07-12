class Solution: 
    #UsingMerge Sort
    def merge(self, nums, l, mid, r):
        a = nums[l:mid+1]
        b = nums[mid+1:r+1]
        
        i = 0
        j = 0
        k = l
        
        while k <= r:
            if j == len(b):
                nums[k] = a[i]
                i += 1
                k += 1
            elif i == len(a):
                nums[k] = b[j]
                j += 1
                k += 1
            elif a[i] < b[j]:
                nums[k] = a[i]
                i += 1
                k += 1
            else:
                nums[k] = b[j]
                j += 1
                k += 1

    def mergeSort(self, nums, l, r):
        # base case
        if l >= r:
            return
        
        # recursive case
        mid = (l + r) // 2
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid+1, r)
        self.merge(nums, l, mid, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums
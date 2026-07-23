'''class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
       #Time Complexity: O(n³)
        n = len(nums)
        seen = set(nums)  # covers i==j or j==k cases (duplicates cancel out)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    seen.add(nums[i] ^ nums[j] ^ nums[k])

        return len(seen)'''

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        #Time Complexity: O(1)
        n = len(nums)

        if n < 3:
            return n

        return 1 << n.bit_length()
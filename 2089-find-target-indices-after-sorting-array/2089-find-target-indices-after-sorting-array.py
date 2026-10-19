class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Approach : Counting
        smaller = 0
        equal = 0

        for num in nums:
            if num < target:
                smaller += 1
            elif num == target:
                equal += 1

        return list(range(smaller, smaller + equal))
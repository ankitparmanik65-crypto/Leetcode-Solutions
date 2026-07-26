class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square = []
        for num in nums:
            square.append(num * num)
        square.sort()
        return square
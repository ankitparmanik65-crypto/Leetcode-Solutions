class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minimum = min(nums)
        maximum = max(nums)

        seen = set(nums)
        answer = []

        for num in range(minimum + 1, maximum):
            if num not in seen:
                answer.append(num)

        return answer
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []

        for num in nums:
            index = abs(num) - 1

            if nums[index] < 0:
                answer.append(abs(num))
            else:
                nums[index] = -nums[index]

        return answer
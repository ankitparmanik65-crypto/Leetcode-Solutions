class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        seen = set()
        answer = 0

        for num in nums:
            if num in seen:
                answer ^= num
            else:
                seen.add(num)

        return answer        
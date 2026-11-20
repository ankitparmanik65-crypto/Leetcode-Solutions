class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        # Sorting + Dynamic Programming
        nums.sort()

        dp0 = {}
        dp1 = {}

        ans = 0

        for num in nums:

            dp1[num + 1] = max(
                dp0.get(num, 0),
                dp1.get(num, 0)
            ) + 1

            dp0[num] = max(
                dp0.get(num - 1, 0),
                dp1.get(num - 1, 0)
            ) + 1

            ans = max(ans, dp0[num], dp1[num + 1])

        return ans

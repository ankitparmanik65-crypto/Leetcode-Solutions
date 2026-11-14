class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # Sliding Window
        n = len(nums)
        ans = float('inf')

        for length in range(l, r + 1):

            curr_sum = sum(nums[:length])

            if curr_sum > 0:
                ans = min(ans, curr_sum)

            for i in range(length, n):

                curr_sum -= nums[i - length]
                curr_sum += nums[i]

                if curr_sum > 0:
                    ans = min(ans, curr_sum)

        return ans if ans != float('inf') else -1

class Solution:
    def maxLength(self, nums: List[int]) -> int:
       # Brute Force + GCD and LCM
        n = len(nums)
        ans = 0

        for i in range(n):

            product = 1
            gcd_value = 0
            lcm_value = 1

            for j in range(i, n):

                num = nums[j]

                product *= num

                gcd_value = gcd(gcd_value, num)

                lcm_value = (lcm_value * num) // gcd(lcm_value, num)

                if product == gcd_value * lcm_value:
                    ans = max(ans, j - i + 1)

        return ans
 
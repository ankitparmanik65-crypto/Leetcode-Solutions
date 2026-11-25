class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        # Binary Search + Double Rolling Hash
        n = len(nums)

        MOD1 = 10**9 + 7
        MOD2 = 10**9 + 9

        BASE1 = 911382323
        BASE2 = 972663749

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)

        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)

        for i in range(n):
            pow1[i + 1] = (pow1[i] * BASE1) % MOD1
            pow2[i + 1] = (pow2[i] * BASE2) % MOD2

            pref1[i + 1] = (
                pref1[i] * BASE1 + nums[i]
            ) % MOD1

            pref2[i + 1] = (
                pref2[i] * BASE2 + nums[i]
            ) % MOD2

        def hasUnique(length):

            freq = {}

            for i in range(n - length + 1):

                h1 = (
                    pref1[i + length]
                    - pref1[i] * pow1[length]
                ) % MOD1

                h2 = (
                    pref2[i + length]
                    - pref2[i] * pow2[length]
                ) % MOD2

                key = (h1, h2)

                freq[key] = freq.get(key, 0) + 1

            return any(count == 1 for count in freq.values())

        left = 1
        right = n

        while left < right:

            mid = (left + right) // 2

            if hasUnique(mid):
                right = mid

            else:
                left = mid + 1

        return left
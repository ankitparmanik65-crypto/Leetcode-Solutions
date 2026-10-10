class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int],
                         k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2

            needed = sum(max(d - mid, 0) for d in diff)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        remaining = k

        for i in range(len(diff)):
            if diff[i] > level:
                remaining -= diff[i] - level
                diff[i] = level

        diff.sort(reverse=True)

        i = 0
        while remaining > 0 and i < len(diff):
            if diff[i] > 0:
                diff[i] -= 1
                remaining -= 1
            else:
                break

            if i + 1 < len(diff) and diff[i] < diff[i + 1]:
                i += 1

        return sum(d * d for d in diff)
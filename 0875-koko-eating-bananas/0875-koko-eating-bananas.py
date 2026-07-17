class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r

        while l <= r:
            k = (l + r) // 2
            hours_needed = self.calculateHours(piles, k)

            if hours_needed <= h:
                ans = k
                r = k - 1
            else:
                l = k + 1

        return ans

    def calculateHours(self, piles, k):
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile / k)
        return total_hours
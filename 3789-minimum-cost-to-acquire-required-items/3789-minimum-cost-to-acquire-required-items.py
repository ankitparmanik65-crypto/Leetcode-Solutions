class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        common = min(need1, need2)

        totalCost = common * min(costBoth, cost1 + cost2)

        remaining1 = need1 - common
        remaining2 = need2 - common

        totalCost += remaining1 * min(cost1, costBoth)
        totalCost += remaining2 * min(cost2, costBoth)

        return totalCost
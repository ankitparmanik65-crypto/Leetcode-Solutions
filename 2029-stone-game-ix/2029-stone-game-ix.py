class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        c0, c1, c2 = count

        if c0 % 2 == 0:
            if c1 > 0 and c2 > 0:
                return True
            else:
                return False

        if abs(c1 - c2) > 2:
            return True
        else:
            return False


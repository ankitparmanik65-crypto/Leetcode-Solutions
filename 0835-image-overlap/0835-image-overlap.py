class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        count = Counter()

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    for x in range(n):
                        for y in range(n):
                            if img2[x][y] == 1:
                                dx = i - x
                                dy = j - y
                                count[(dx, dy)] += 1

        return max(count.values(), default=0)        
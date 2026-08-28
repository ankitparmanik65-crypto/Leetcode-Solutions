class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1
        
        left = min(bloomDay)
        right = max(bloomDay)

        while left <= right:
            mid = (left + right) // 2
            flower = 0
            boukets = 0

            for bloom in bloomDay:
                if bloom <= mid:
                    flower += 1

                    if flower == k:
                        boukets += 1
                        flower = 0
                else:
                    flower = 0
            
            if boukets >= m:
                right = mid - 1
            else:
                left = mid + 1
        return left 
class Solution:
    def countCommas(self, n: int) -> int:
        answer = 0
        separator = 1000
        while separator <= n:
            answer += n - separator + 1
    
            separator *= 1000

        return answer       
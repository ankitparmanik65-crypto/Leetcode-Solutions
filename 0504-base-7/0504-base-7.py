class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        if num < 0 :
            sign = "-"
        else :
            sign = ""

        num = abs(num)

        result = []

        while num > 0:
            digit = num % 7
            result.append(str(digit))
            num //= 7

        result.reverse()
        answer = "".join(result)

        return sign + answer


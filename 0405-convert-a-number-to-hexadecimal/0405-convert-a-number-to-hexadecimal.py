class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        result = []
        num &= 0xFFFFFFFF

        while num:
            digit = num & 0xF

            if digit < 10:
                result.append(chr(ord('0') + digit))
            else:
                result.append(chr(ord('a') + digit - 10))

            num >>= 4

        return ''.join(result[::-1])        
class Solution:
    def replaceDigits(self, s: str) -> str:
        chars = list(s)

        for i in range(1, len(s), 2): #Only Odd Indices
            digit = int(s[i])
            chars[i] = chr(ord(s[i - 1]) + digit)

        return "".join(chars)
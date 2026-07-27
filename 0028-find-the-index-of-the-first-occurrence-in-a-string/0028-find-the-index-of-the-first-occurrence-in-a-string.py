class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            window = haystack[i:i + m] # Start index = i, End index = i + m

            if window == needle:
                return i

        return -1
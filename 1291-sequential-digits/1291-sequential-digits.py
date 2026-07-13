class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        result = []

        for length in range(2, 10):
            for start in range(0, 10 - length):
                candidate = int(digits[start:start + length])
                if low <= candidate <= high:
                    result.append(candidate)

        result.sort()
        return result
        
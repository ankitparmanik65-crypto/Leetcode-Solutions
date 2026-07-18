class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)

        return self.gcd(smallest, largest)

    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        endswith = [0] * 26  # endswith[i] = subsequences ending with char i
        
        for ch in s:
            idx = ord(ch) - ord('a')
            total = sum(endswith) % MOD
            endswith[idx] = (total + 1) % MOD  # overwrite, not add!
        
        return sum(endswith) % MOD        
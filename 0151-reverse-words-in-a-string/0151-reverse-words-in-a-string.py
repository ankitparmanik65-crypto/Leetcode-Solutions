class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1 - Split
        words = s.split()

        # Step 2 - Reverse
        i = 0
        j = len(words) - 1
        while i < j:
            words[i], words[j] = words[j], words[i]
            i += 1
            j -= 1

        # Step 3 - Join
        return " ".join(words)
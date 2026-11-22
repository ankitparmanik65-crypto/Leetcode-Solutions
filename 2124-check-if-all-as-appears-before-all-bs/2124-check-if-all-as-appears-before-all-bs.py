class Solution:
    def checkString(self, s: str) -> bool:
        # String Traversal (Single Pass)
        found_b = False

        for ch in s:

            if ch == 'b':
                found_b = True

            elif ch == 'a' and found_b:
                return False

        return True

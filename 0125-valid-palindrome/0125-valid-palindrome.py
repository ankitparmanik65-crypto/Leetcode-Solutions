class Solution:
    def isAlphanumeric(self, charcter):
        return (ord('a') <= ord(charcter) <= ord('z') or
                ord('0') <= ord(charcter) <= ord('9'))
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        i = 0
        j = len(s) - 1

        while i < j:
            if not self.isAlphanumeric(s[i]):
                i += 1
            elif not self.isAlphanumeric(s[j]):
                j -= 1
            elif s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True

    
        
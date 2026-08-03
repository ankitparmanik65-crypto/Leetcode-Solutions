class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        #Using Slicing
        for word in words:
            if word == word[::-1]:
                return word

        return ""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #Built-in Approach -> collections.Counter() 
        #return not (Counter(ransomNote) - Counter(magazine))
        
        #Frequency Counting
        if len(ransomNote) > len(magazine):
            return False

        count = [0] * 26   #for 'a' to 'z'

        for ch in magazine:
            count[ord(ch) - ord('a')] += 1

        for ch in ransomNote:
            count[ord(ch) - ord('a')] -= 1
            if count[ord(ch) - ord('a')] < 0:
                return False

        return True
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        #Concatination
        if len(s) != len(goal):
            return False

        return goal in (s + s)
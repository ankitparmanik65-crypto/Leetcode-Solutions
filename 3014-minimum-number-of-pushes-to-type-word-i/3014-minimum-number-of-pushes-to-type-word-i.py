class Solution:
    def minimumPushes(self, word: str) -> int:
        pushes = 0
        n = len(word)

        for i in range(n):
            pushes += (i // 8) + 1

        return pushes
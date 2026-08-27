class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for i in range(n - 1, -1, -1):
            temp = count[:]

            for j in range(i):
                idx = ord(target[j]) - ord('a')
                temp[idx] -= 1
                if temp[idx] < 0:
                    break
            else:
                idx = ord(target[i]) - ord('a')

                for bigger in range(idx + 1, 26):
                    if temp[bigger] > 0:
                        temp[bigger] -= 1

                        result = target[:i] + chr(bigger + ord('a'))

                        for c in range(26):
                            result += chr(c + ord('a')) * temp[c]

                        return result

        return ""
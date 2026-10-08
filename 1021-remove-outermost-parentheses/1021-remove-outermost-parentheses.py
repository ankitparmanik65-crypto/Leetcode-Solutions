class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance = 0
        result = []

        for c in s:
            if c == '(':
                if balance > 0:
                    result.append(c)
                balance += 1
            else:
                balance -= 1
                if balance > 0:
                    result.append(c)

        return ''.join(result)
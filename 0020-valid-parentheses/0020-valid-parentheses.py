class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for ch in s:
            # opening brackets
            if ch == '(' or ch == '{' or ch == '[':
                st.append(ch)
            # closing brackets
            else:
                if len(st) == 0:
                    return False

                top = st.pop()

                if ch == ')' and top != '(':
                    return False
                elif ch == '}' and top != '{':
                    return False
                elif ch == ']' and top != '[':
                    return False

        if len(st) == 0:
            return True 
        else:
            return False
        
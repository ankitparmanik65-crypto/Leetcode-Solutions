class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        st = []
        seen = set()

        for ch in s:
            count[ch] -= 1

            if ch in seen:
                continue

            while st and st[-1] > ch and count[st[-1]] > 0:
                removed = st.pop()
                seen.remove(removed)

            st.append(ch)
            seen.add(ch)

        return ''.join(st)
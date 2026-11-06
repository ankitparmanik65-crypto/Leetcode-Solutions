class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda log: log[1])
        sorted_queries = sorted(
            (q, i) for i, q in enumerate(queries)
        )

        ans = [0] * len(queries)
        count = defaultdict(int)

        left = right = 0
        m = len(logs)

        for q, idx in sorted_queries:
            start = q - x

            while right < m and logs[right][1] <= q:
                server = logs[right][0]
                count[server] += 1
                right += 1

            while left < m and logs[left][1] < start:
                server = logs[left][0]
                count[server] -= 1

                if count[server] == 0:
                    del count[server]

                left += 1

            ans[idx] = n - len(count)

        return ans
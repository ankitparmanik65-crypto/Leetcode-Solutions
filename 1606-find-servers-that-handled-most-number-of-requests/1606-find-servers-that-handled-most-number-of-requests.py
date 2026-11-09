class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        def update(index, value):
            pos = size + index
            tree[pos] = value

            pos //= 2
            while pos:
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]
                pos //= 2

        def find_first(node, left, right, ql, qr):
            if right <= ql or left >= qr or tree[node] == 0:
                return -1

            if right - left == 1:
                return left if left < k else -1

            mid = (left + right) // 2

            result = find_first(
                node * 2, left, mid, ql, qr
            )

            if result != -1:
                return result

            return find_first(
                node * 2 + 1, mid, right, ql, qr
            )

        busy = []
        counts = [0] * k

        for i, (start, duration) in enumerate(zip(arrival, load)):

            while busy and busy[0][0] <= start:
                _, server = heapq.heappop(busy)
                update(server, 1)

            preferred = i % k

            server = find_first(
                1, 0, size, preferred, k
            )

            if server == -1:
                server = find_first(
                    1, 0, size, 0, preferred
                )

            if server == -1:
                continue

            update(server, 0)
            counts[server] += 1

            heapq.heappush(
                busy, (start + duration, server)
            )

        maximum = max(counts)

        return [
            i for i in range(k)
            if counts[i] == maximum
        ] 
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []

        current_time = 0

        for j, task in enumerate(tasks):
            current_time = max(current_time, j)

            while busy and busy[0][0] <= current_time:
                finish_time, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            if not available:
                current_time = busy[0][0]

                while busy and busy[0][0] <= current_time:
                    finish_time, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            weight, index = heapq.heappop(available)

            ans.append(index)

            finish_time = current_time + task
            heapq.heappush(busy, (finish_time, weight, index))

        return ans
class MyStack:
    def __init__(self):
        self.queue1 = deque()

    def push(self, x: int) -> None:
        self.queue1.append(x)
        size = len(self.queue1)

        # rotate the queue so the newly pushed element moves to the front
        for i in range(size - 1):
            front = self.queue1.popleft()
            self.queue1.append(front)

    def pop(self) -> int:
        return self.queue1.popleft()

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
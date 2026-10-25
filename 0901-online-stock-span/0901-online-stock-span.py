class StockSpanner:

    def __init__(self):
        self.st = []   # stack of (price, span) pairs

    def next(self, price: int) -> int:
        span = 1

        while len(self.st) > 0 and self.st[-1][0] <= price:
            prevPrice, prevSpan = self.st.pop()
            span += prevSpan

        self.st.append((price, span))

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
class StockSpanner:

    def __init__(self):
        self.st = []
        self.idx = -1

    def next(self, price: int) -> int:
        
        while self.st and self.st[-1][0] <= price:
            self.st.pop()
        self.idx += 1
        ans = self.idx - (self.st[-1][1] if self.st else -1)
        self.st.append( [price, self.idx] )
        print(self.st)

        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
class StockSpanner:

    def __init__(self):
        self.l = []
        self.idx = -1
    def next(self, price: int) -> int:
        # span = 0
        temp = []
        while self.l and self.l[-1][0] <= price:
            # span += 1
            temp.append(self.l.pop())
        prevGreIdx = -1
        if self.l:
            prevGreIdx = self.l[-1][1]
        ans = self.idx-prevGreIdx+1
        self.idx+=1
        self.l.append([price,self.idx])
        return ans
        # while temp:
        #     self.l.append(temp.pop())
        # self.l.append([price,span+1])
        # d[price] = span+1
        # return span+1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price) 
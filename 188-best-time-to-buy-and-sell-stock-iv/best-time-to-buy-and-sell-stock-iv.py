class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        INF = 10**20
        cache = {}
        def rec(idx,can_buy,tran):
            if (idx,can_buy,tran) in cache:
                return cache[(idx,can_buy,tran)]
            if idx == n or tran == 0:
                return 0
            profit = -INF
            if can_buy:
                profit = max(profit,-prices[idx] + rec(idx+1, 0, tran))
                profit = max(profit, rec(idx+1, 1, tran))
            else:
                profit = max(profit, prices[idx] + rec(idx+1, 1, tran-1))
                profit = max(profit, rec(idx+1, 0, tran))
            cache[(idx,can_buy,tran)] = profit
            return profit
        return rec(0,1,k)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = {}
        def rec(idx,can_buy,tran):
            if (idx,can_buy,tran) in cache:
                return cache[(idx,can_buy,tran)]
            if idx == n or tran == 0:
                return 0
            profit = 0
            if can_buy:
                profit = max(profit,-prices[idx]+rec(idx+1,0,tran)) #buy
                profit = max(profit,rec(idx+1,1,tran))              #skip
            else:
                profit = max(profit,prices[idx]+rec(idx+1,1,tran-1))    #sell
                profit = max(profit,rec(idx+1,0,tran))                  #skip
            cache[(idx,can_buy,tran)] = profit
            return profit
        
        return rec(0,1,2)
        
            



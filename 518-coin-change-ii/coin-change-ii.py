class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        @cache
        def rec(amt,idx):
            if amt == 0:
                return 1
            if amt < 0:
                return 0
            if idx == n:
                return 0
            cnt = 0
            # for i in range(idx,n):
            cnt += rec(amt-coins[idx],idx)
            cnt += rec(amt,idx+1)
            
            return cnt
        return rec(amount,0)
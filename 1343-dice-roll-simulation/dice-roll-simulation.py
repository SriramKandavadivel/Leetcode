class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        m = len(rollMax)
        MOD = 10**9+7
        @cache
        def rec(t,prev):
            if t < 0:
                return 0
            if t== 0:
                return 1 
            res = 0
            for i in range(1,7):
                if prev != i:
                    for j in range(1,rollMax[i-1]+1):
                        res += rec(t-j,i)
            return res%MOD
        return rec(n,-1)
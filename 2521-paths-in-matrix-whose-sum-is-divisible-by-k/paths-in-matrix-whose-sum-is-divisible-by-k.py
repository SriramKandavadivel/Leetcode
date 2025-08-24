class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9+7
        m,n = len(grid),len(grid[0])
        @cache
        def rec(i,j,s):
            # if i >= m or j >= n:
            #     return 0
            if i == m-1 and j == n-1:
                val = grid[i][j] 
                s += val
                if s % k == 0:
                    return 1
                return 0
            cnt = 0
            val = grid[i][j] 
            # s %= k
            if i+1 < m:
                cnt += (rec(i+1,j,(s+val)%k)) 
            if j+1 < n:
                cnt += (rec(i,j+1,(s+val)%k)) 
            return cnt % MOD
        # return rec(0,0,0)
    
    
        dp = [[[0 for i in range(k)]for j in range(n)]for z in range(m)]
        dp[m-1][n-1][(k-(grid[m-1][n-1]%k))%k] = 1

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                val = grid[i][j]
                for s in range(k):
                    if i == m-1 and j == n-1 and s == (k-(grid[i][j]%k))%k:
                        continue
                    cnt = 0
                    if i+1 < m:
                        cnt += dp[i+1][j][(s+val)%k]
                    if j+1 < n:
                        cnt += dp[i][j+1][(s+val)%k]
                    dp[i][j][s] = cnt % MOD 
        return dp[0][0][0]
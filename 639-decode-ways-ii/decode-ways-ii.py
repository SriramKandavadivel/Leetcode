class Solution:
    def numDecodings(self, s: str) -> int:
        # MOD = 10**9+7
        # n = len(s)
        # @cache
        # def rec(idx):
        #     if idx == n:
        #         return 1
        #     if idx > n:
        #         return 0
        #     if s[idx] == '0':
        #        return 0
            
        #     cnt = 0
        #     cnt += rec(idx+1)
        #     if s[idx] == '*':
        #         cnt += 8 * rec(idx+1)
        #         # print(cnt)
        #         if idx+1 < n and s[idx+1] == '*':
        #             cnt += 15 * rec(idx+2)
        #         elif idx+1 < n and s[idx+1] != '*':
        #             cnt += rec(idx+2)
        #         if idx+1 < n and s[idx+1] != '*' and 0 <= int(s[idx+1]) <= 6:
        #             cnt += rec(idx+2)
                
        #     if s[idx] == '1':
        #         if idx+1 < n and s[idx+1] == '*':
        #             cnt += 9 * rec(idx+2)
        #         elif idx+1 < n and s[idx+1] != '*':
        #             cnt += rec(idx+2) 
        #     if s[idx] == '2':
        #         if idx+1 < n and s[idx+1] == '*':
        #             cnt += 6 * rec(idx+2)
        #         elif idx+1 < n and s[idx+1] != '*' and 0 <= int(s[idx+1]) <= 6:
        #             cnt += rec(idx+2)
            
        #     return cnt % MOD
        # return rec(0)
        MOD = 10**9+7
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1

        for idx in range(n-1,-1,-1):
            if s[idx] == '0':
                continue

            cnt = 0
            cnt += dp[idx+1]
            if s[idx] == '*':
                cnt += 8*dp[idx+1]
                if idx+1 < n and s[idx+1] == '*':
                    cnt += 15*dp[idx+2]
                elif idx+1 < n and s[idx+1] != '*':
                    cnt += dp[idx+2]
                if idx +1 < n  and s[idx+1] != '*' and  0 <= int(s[idx+1]) <= 6:
                    cnt += dp[idx+2]
                
            if s[idx] == '1':
                if idx+1 < n and s[idx+1] == '*':
                    cnt += 9*dp[idx+2]
                elif idx+1 < n and s[idx+1] != '*':
                    cnt += dp[idx+2]
            if s[idx] == '2':
                if idx+1 < n and s[idx+1] == '*':
                    cnt += 6*dp[idx+2]
                elif idx+1 < n   and '0' <= (s[idx+1]) <= '6':
                    cnt += dp[idx+2]
            
            dp[idx]  = cnt%MOD

        return dp[0] % MOD
        

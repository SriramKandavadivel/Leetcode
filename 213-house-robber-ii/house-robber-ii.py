class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        INF = 10**20
        if n == 1:
            return nums[0]
        # def rec(arr):
        #     x = n-1 ##length is same on both cases
        #     dp = [0 for i in range(x)]
        #     for i in range(x-1,-1,-1):
        #         amt = -INF
        #         if i+1 < x:
        #             amt = max(amt,dp[i+1])
        #         val = 0 if i+2 >= x else dp[i+2]
        #         amt = max(amt,val + arr[i])

        #         dp[i] = amt
        #     return dp[0]

        # return max( rec(nums[:n-1]), rec(nums[1:]) )
        def hr2(arr):
            l = len(arr)
            @cache
            def rec(idx):
                if idx >= l:
                    return 0
                ans = -INF
                ans = max(ans,rec(idx+1))
                ans = max(ans, arr[idx]+rec(idx+2))

                return ans
            return rec(0)
        return max( hr2(nums[:n-1]) , hr2(nums[1:]) )

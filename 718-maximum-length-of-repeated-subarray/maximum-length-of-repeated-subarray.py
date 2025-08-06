class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # m,n = len(nums1),len(nums2)
        # ans = 0
        # @cache
        # def rec(i,j):
        #     if i == m or j == n:
        #         return 0
            
        #     cnt = 0
        #     if nums1[i] == nums2[j]:
        #         cnt = max(cnt, 1+rec(i+1,j+1))
        #     return cnt

        # for i in range(m):
        #     for j in range(n):
        #         if nums1[i] == nums2[j]:
        #             ans = max(ans,rec(i,j))

        # return ans

        m,n = len(nums1),len(nums2)
        dp = [[0 for i in range(n+1)]for j in range(m+1)]
        # dp[m][n] = 0
        ans = 0
        for i in range(m-1,-1,-1):
            for j in  range(n-1,-1,-1):
                cnt = 0
                if nums1[i] == nums2[j]:
                    cnt = max(cnt, 1+dp[i+1][j+1])
                dp[i][j] = cnt
                ans = max(ans, dp[i][j])
        return ans 
            
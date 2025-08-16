class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        n = len(nums)
        @cache
        def rec(idx,prev):
            if idx == n:
                return 0
            ans = 0
            # for i in range(idx,n):
            if prev == nums[idx]%2:
                ans = max(ans, nums[idx]+ rec(idx+1, nums[idx]%2))
            elif prev != nums[idx]%2:
                ans = max(ans, (nums[idx]-x)+ rec(idx+1, nums[idx]%2))
            ans = max(ans,rec(idx+1, prev))
            
            return ans
        
        return rec(1,nums[0]%2)+nums[0]
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prod = 1
        l = r= 0
        cnt = 0
        while r < n:
            prod *= nums[r]
            while l <= r and prod >= k:
                prod = prod//nums[l]
                l += 1
            cnt += (r-l+1)
            r+=1
        return cnt
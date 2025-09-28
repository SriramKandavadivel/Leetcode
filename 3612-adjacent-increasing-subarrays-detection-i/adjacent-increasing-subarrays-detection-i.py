class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        i,j = 0,k
        cnt = 0
        if k == 1:
            return True
        while j < n-1:
            if nums[i+1] - nums[i] > 0 and nums[j+1] - nums[j] > 0:
                cnt += 1
            else:
                cnt = 0
            
            if cnt+1 == k:
                return True
            i += 1
            j += 1
        return False
                
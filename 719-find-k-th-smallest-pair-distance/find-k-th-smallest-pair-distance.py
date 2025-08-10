class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        
        def isSafe(val):
            i,j = 0,0
            cnt = 0
            while i < n:
                while j < n and abs(nums[j]-nums[i]) <= val:
                    j+=1
                cnt += (j-i-1)
                i += 1
            return cnt >= k
        l = 0
        r = nums[n-1]-nums[0]
        ans = 0
        while l <= r:
            m = (l+r)//2
            if isSafe(m):
                ans = m
                r = m-1
            else:
                l = m+1
        return ans

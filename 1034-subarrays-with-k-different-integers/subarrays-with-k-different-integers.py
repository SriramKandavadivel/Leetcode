class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def atleast(x):
            d = collections.defaultdict(lambda : 0)
            l = r = 0
            cnt = 0
            while l < n:
                while r < n and len(d) < x:
                    d[nums[r]] += 1
                    r += 1
                if len(d) >= x:
                    cnt += (n-r)+1
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    del d[nums[l]]
                l += 1
            return cnt
        
        return atleast(k) - atleast(k+1)
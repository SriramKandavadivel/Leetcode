class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n= len(nums)
        d = collections.defaultdict(lambda : 0)
        l = 0
        r = 0
        tot = 0
        while r < n:
            d[nums[r]] += 1
            while l <= r and len(d) > k:
                
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    del d[nums[l]]
                l += 1
            tot += (r-l+1)
            r += 1
        atmostk = tot
        r = 0
        l = 0
        val = 0
        d = collections.defaultdict(lambda : 0)
        while r < n:
            d[nums[r]] += 1
            while l <= r and len(d) > k-1:
                d[nums[l]] -= 1
                if d[nums[l]]== 0:
                    del d[nums[l]]
                l += 1
                
            val += (r-l+1)
            r += 1 
             
        atmostk1 = val
            
        print(atmostk,atmostk1)
        return abs(atmostk - atmostk1)

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n= len(nums)
        def rec(x):
            d = collections.defaultdict(lambda : 0)
            l = 0
            r = 0
            cnt = 0
            while l < n:
                while r < n and len(d) < x:
                    d[nums[r]] += 1
                    r += 1
                    print(l,r)
                if len(d) >= x:
                    cnt += n - r+1
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    del d[nums[l]]
                l += 1
            # print(cnt)
            return cnt
        
        return rec(k)-rec(k+1)

"""
##atmost - while r < n:
            tot += nums[r]
            while tot > k:
                tot -= l
                l+=1
            ans = r-l+1
            r+=1
##atleast  - while l < n:
                while r < n and tot < k:
                    tot += nums[r]
                    r+=1
                tot -= nums[l]
                l += 1
"""

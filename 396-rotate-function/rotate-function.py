class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        INF = 10**20
        s = 0
        v = 0
        n = len(nums)
        for i in range(n):
            s += nums[i]
            v += i*nums[i]
        res = -INF
        
        # print(s)
        for i in range(n-1,-1,-1):
            v += s+ (-(n)*nums[i])
            res = max(v,res)
            print(v)
        return res
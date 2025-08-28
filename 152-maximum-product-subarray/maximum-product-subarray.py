class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        INF = 10**20
        max_,min_ = 1,1
        res = -INF
        for num in nums:
            if num == 0:
                res = max(num,res)
                max_ = 1
                min_ = 1
                continue
            a = max(max_ * num, min_ * num, num)
            b = min(max_ * num, min_ * num, num)
            max_ = a
            min_ = b
            print(max_,min_)
            res = max(res,min_, max_)
        return res
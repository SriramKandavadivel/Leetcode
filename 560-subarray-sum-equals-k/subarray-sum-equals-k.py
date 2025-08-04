class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        tot = 0
        d = {0:1}
        cnt = 0
        for i,val in enumerate(nums):
            tot += val
            if tot-k in d:
                cnt += d[tot-k]
            if tot not in d:
                d[tot] = 1
            elif tot in d:
                d[tot] += 1
        return cnt
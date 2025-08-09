class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = []
        for num in nums:
            idx = bisect.bisect_right(l,num)
            if idx ==len(l):
                l.append(num)
            else:
                l[idx] = num
        return len(nums) - len(l)

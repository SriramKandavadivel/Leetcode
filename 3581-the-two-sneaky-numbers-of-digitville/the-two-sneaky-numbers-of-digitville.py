class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        n = len(nums)
        l = set()
        for i in range(n):
            if d[nums[i]] > 1:
                l.add(nums[i])
        return list(l)
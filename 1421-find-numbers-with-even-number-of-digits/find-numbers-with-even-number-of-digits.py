class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for x in nums:
            n = str(x)
            m = len(n)
            if m % 2 == 0:
                cnt += 1
        return cnt
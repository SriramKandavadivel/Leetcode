class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        # i,j,k = 0,n-2,n-1
        med = 0
        nums = deque(nums)

        while nums:
            nums.popleft()
            nums.pop()
            med += nums.pop()
        return med
        

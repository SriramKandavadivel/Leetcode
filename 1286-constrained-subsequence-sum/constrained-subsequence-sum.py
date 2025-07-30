class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        val = 0
        wind = deque([])
        for i in range(n):
            nums[i] += (wind[0] if wind else 0 )
            while wind and wind[-1] < nums[i]:
                wind.pop()

            if nums[i] > 0:
                wind.append(nums[i])
            
            if i>=k and wind and wind[0] == nums[i-k]:
                wind.popleft()
        return max(nums)
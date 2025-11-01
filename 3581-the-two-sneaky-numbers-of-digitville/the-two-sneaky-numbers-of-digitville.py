class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # n = n-2
        # print(n)
        for i,x in enumerate(nums):
            nums[i] += 1
        print(nums)
        res = []
        for i,x in enumerate(nums):
            if nums[abs(x)-1] < 0:
                res.append(abs(x)-1)
                # print(i,x-1, nums[x-1])
            
            nums[abs(x)-1] = -1* nums[abs(x)-1]
        print(nums[:-2])
        return res
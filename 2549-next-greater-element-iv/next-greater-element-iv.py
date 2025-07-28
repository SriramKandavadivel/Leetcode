class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1]*n
        sec_gre = [] 
        fir_gre = [] 
        for i in range(n):
            while sec_gre and nums[sec_gre[-1]] < nums[i]:
                res[sec_gre.pop()] = nums[i]

            temp = []
            while fir_gre and nums[fir_gre[-1]] < nums[i]:
                temp.append(fir_gre.pop())
            sec_gre += temp[::-1]
            fir_gre.append(i)
        return res
        
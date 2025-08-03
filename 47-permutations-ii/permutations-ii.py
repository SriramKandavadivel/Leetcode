class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        l = []
        ans = []
        used = [False]*n

        def rec(l):
            nonlocal ans
            # if idx == n:
            #     return
            if len(l) == n and l not in ans:
                print(l)
                ans.append(list(l))
                return
            for i in range(n):
                if used[i]:
                    continue

                used[i] = True    
                l.append(nums[i])
                rec(l)
                l.pop()
                used[i] = False
            
            # return ans
        rec([])
        return ans
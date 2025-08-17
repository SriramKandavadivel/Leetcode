class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        l = []
        ans = []
        def rec(rem,idx):
            if rem < 0:
                return
            if rem == 0 and l not in ans:
                ans.append(list(l))
                return
            for i in range(idx,n):
                l.append(candidates[i])
                rec(rem-candidates[i],i)
                l.pop()
            return 
        
        rec(target,0)
        # print(ans)
        return ans
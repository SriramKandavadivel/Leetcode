class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        l = []
        ans = []
        def rec(sum_,idx):
            if sum_ > target:
                return
            
            if sum_ == target:
                x = sorted(l)
                if x not in ans:
                    ans.append(x)
                return
            for i in range(idx,n):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                l.append(candidates[i])
                # print(l)
                rec(sum_ +candidates[i], i+1)
                l.pop()
            return
        rec(0,0)
        return ans
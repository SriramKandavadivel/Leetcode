class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        forward_lis = [0]*n  ###len of lis
        backward_lis = [0]*n    ###len of lds
        l1 = []
        for i in range(n):
            idx = bisect.bisect_left(l1, nums[i])
            if len(l1) == idx:
                l1.append(nums[i])
            else:
                l1[idx] = nums[i]
        
            forward_lis[i] = idx+1   ##len of curr lis

        l2 = [] 
        for j in range(n-1,-1,-1):
            idx = bisect.bisect_left(l2,nums[j])
            if len(l2) == idx:
                l2.append(nums[j])
            else:
                l2[idx] = nums[j]

            backward_lis[j] = idx+1     ###len of curr lds

        min_del = 1000
        for i in range(1,n-1):
            if forward_lis[i] > 1 and backward_lis[i] > 1:
                min_del = min(min_del, n-(forward_lis[i]+backward_lis[i]-1))
        return min_del       
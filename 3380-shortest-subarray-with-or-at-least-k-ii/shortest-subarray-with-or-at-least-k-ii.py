class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        arr = [0]*32
        INF = 10**20
        ans = INF        
        if k ==0 :
            return 1 if max(nums)>=k else -1
        def Value():
            m = []
            for num in arr:
                if num >0:
                    m.append(1)
                else:
                    m.append(0)
            return int("".join(map(str,m)), 2)
        def add(val,isadd):
            # val = bin(val)
            # print(bin(val))
            val = bin(val)[2:]
            val = '0' * (32-len(val)) + val
            for i in range(32):
                if val[i] == '1':
                    if isadd:
                        arr[i] += 1
                    else:
                        arr[i] -= 1
        l = r = 0
        while l < n:
            while r < n and Value() < k:
                add(nums[r], True)
                r += 1
            if Value() >= k:
                ans = min(ans,r-l)
            add(nums[l], False)
            l += 1
        return ans if ans != INF else -1
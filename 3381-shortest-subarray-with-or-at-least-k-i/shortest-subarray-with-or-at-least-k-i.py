class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        INF = 10**20
        arr = [0]*32
        if k == 0:
            return 1 if max(nums) >= k else -1
        def add(val , canAdd):
            x = bin(val)[2:]
            x = '0'*(32-len(x)) + x
            for i in range(32):
                if x[i] == '1':
                    if canAdd:
                        arr[i] += 1
                    else:
                        arr[i] -= 1
        def Value():
            m = []
            for y in arr:
                if y > 0:
                    m.append('1')
                else:
                    m.append('0')
            return int(''.join(m),2)        
        
        ans = INF
        l = r = 0
        while l < n:
            while r < n and Value() < k:
                add(nums[r], True)
                r += 1
            if Value() >= k:
                ans = min(ans, r-l)
            add(nums[l], False)  ###subtract
            l += 1
        return ans if ans != INF else -1
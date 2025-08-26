class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i,v in enumerate(arr):
            tot_sub = (i+1) * (n-i)
            odd_cnt = (tot_sub+1) // 2
            ans += odd_cnt * v
        return ans

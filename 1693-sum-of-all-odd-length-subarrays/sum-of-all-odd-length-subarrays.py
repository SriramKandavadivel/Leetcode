class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(n):
                if (i-j+1) % 2 == 1:
                    for z in range(i,j+1):
                        ans += arr[z]
        return ans
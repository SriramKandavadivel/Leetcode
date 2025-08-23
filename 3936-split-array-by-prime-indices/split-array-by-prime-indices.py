class Solution:
    def splitArray(self, nums: List[int]) -> int:
        l = len(nums)

        N = max(2,l+1) ##minimum keep the 0,1 as false in the array
        
        isPrime = [True]*N
        isPrime[0] = False
        isPrime[1] = False

        for i in range(N):
            if isPrime[i]:   
                for j in range(i+i,N,i):   ### runtime = nlog(n) bcoz loop incrmts i times for evry i
                    isPrime[j] = False
        sum1 = 0
        sum2 = 0    
        for i in range(l):
            if isPrime[i]:
                sum1 += nums[i]
            else:
                sum2 += nums[i]
        
        return abs(sum1-sum2)
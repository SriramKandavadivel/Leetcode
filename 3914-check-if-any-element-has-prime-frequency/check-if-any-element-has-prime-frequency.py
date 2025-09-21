class Solution:

    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        l = len(nums)
        def isprime(num):
            if num == 1 or num == 0:
                return False
            temp  = [True] * (num+1)
            p = 2
            while p * p <= num:
                if temp[p]:
                    for i in range(p*p , num+1, p):
                        temp[i] = False
                p += 1
            if temp[num]:
                return True
            return False

        d = Counter(nums)
        # d = sorted(d)
        print(d)
        for x in nums:
            if isprime(d[x]):
                return True
        return False
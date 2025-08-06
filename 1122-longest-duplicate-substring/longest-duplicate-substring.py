class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        MOD = 10**12+7
        d = 26
        def check(m):
            l = 0
            r = m-1
            hash_val = 0
            for i in range(l,r+1):
                asc = ord(s[i])
                hash_val = ( hash_val + (asc * power[m-1-i]) ) % MOD
                print( power[m-1-i])
            dic = {}
            dic[hash_val] = 0
            while r+1 < n:
                r += 1
                asc = ord(s[l])
                hash_val = (hash_val -(asc * power[m-1]) %MOD) %MOD
                hash_val *= d
                hash_val = (hash_val + ord(s[r]) * 1)%MOD ## d**0 = 1
                l += 1
                if hash_val in dic:
                    return dic[hash_val]
                else:
                    dic[hash_val] = l
            return -1

        power = [0]*n
        power[0] = 1
        for i in range(1,n):
            power[i] = (power[i-1]*d)%MOD
        l=1
        r= n-1
        idx = 0
        wind = 0
        while l <= r:
            m = (l+r)//2
            x = check(m)
            if x == -1:
                r = m-1
            else:

                idx = x
                wind = m
                print(idx,wind)
                l = m+1
        
        return s[idx:idx+wind] 


class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        l=0
        r = k-1
        h_val = 0
        power_ = [0] * n
        power_[0] = 1
        for i in range(1,n):
            power_[i] = power_[i-1] * power
        for i in range(l,r+1):
            asc = ord(s[i])-ord('a')+1
            # print(asc)
            h_val = (h_val + (asc* power_[i])) 
            # print(h_val)
        # print(h_val)
        if (h_val)%modulo == hashValue :
            return s[l:r+1]
        # h_val = h_val%modulo
        while r+1 < n:
            r+=1
            asc = ord(s[l])-ord('a')+1
            h_val = (h_val - (asc* 1))
            h_val = (h_val // power) 
            asc = ord(s[r])-ord('a')+1
            h_val = (h_val + (asc * power_[k-1]) )
            l+=1
            # h_val = h_val%modulo
            if h_val%modulo == hashValue:
                return s[l:r+1]
        return ""
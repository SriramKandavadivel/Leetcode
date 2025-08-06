class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        MOD = 10**12+7
        d = 26
        n = len(s)
        ans = set()
        l = 0
        r = 10-1
        hash_v = 0
        power = [0]*10
        power[0] = 1
        for i in range(1,10):
            power[i] = (power[i-1] * d) % MOD
        for i in range(l,r+1):  ## 0 to 9
            hash_v = (hash_v + ord(s[i]) * power[10-1-i]) %MOD
        dic ={}
        dic[hash_v] = 0
        while r+1 < n:
            r += 1
            hash_v = (hash_v - (ord(s[l])*power[10-1]) %MOD) %MOD
            hash_v *= d
            hash_v = (hash_v + (ord(s[r]) * 1)) %MOD
            l += 1
            if hash_v in dic:
                idx = dic[hash_v]
                ans.add(s[idx: idx+10])
            else:
                dic[hash_v] = l
        return list(ans)
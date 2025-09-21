class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow = ['a','e','i','o','u']
        vow = set(vow)
        
        l = list(s)
        d = Counter(l)
        d= sorted(d.items(), key = lambda val : val[1], reverse = True)
        # print(d)
        freq = 0
        f_v = 1
        f_c = 1
        for key in d:
            if f_v and key[0] in vow:
                f_v = 0
                freq += key[1]
            elif f_c and key[0] not in vow:
                f_c = 0
                freq += key[1]
            # else:
            #     return freq
        return freq
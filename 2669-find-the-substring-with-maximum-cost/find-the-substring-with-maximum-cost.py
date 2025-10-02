class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        d1 = collections.defaultdict(lambda : 0)
        d2  = collections.defaultdict(lambda : 0)
        for i,y in enumerate(chars):
            d2[y] = vals[i]
        for x in s:
            if x in d2:
                d1[x] = d2[x]
            else:
                d1[x] = ( ord(x)- 96 )
        # print(d1['a'])
        tot = 0
        sum_ = 0
        for x in s:
            sum_ += d1[x]
            
            tot = max(tot , sum_)

            sum_ = max(sum_ , 0)
            
        return tot
        
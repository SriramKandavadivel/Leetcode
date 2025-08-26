class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        j = 0
        for x,y in groupby(chars):
            # print(x,list(y))
            chars[j] = x
            j += 1
            l =  len(list(y))
            # print(l)
            if 1 < l <= 9:
                chars[j] = str(l)
                j += 1
            elif l >= 10:
                m = str(l)
                i = 0
                while i < len(m):
                    print(chars,j)
                    chars[j] = m[i]
                    j += 1
                    i += 1
                
        return j 
        # j = 0
        # d = collections.defaultdict(lambda:0)
        # for i in range(n):
        #     if chars[i] not in d:
        #         if len(d) == 1:
        #             chars[j] = chars[i-1]
        #             j+=1
        #             if d[chars[i-1]] > 1:
        #                 chars[j] = d[chars[i-1]]
        #                 j+=1
                    
        #             del d[chars[i-1]]
        #             # d.clear()
        #         d[chars[i]] += 1
        #     elif chars[i] in d:
        #         d[chars[i]] += 1
        # return j
class Solution:
    def maxDifference(self, s: str) -> int:
        l = list(s)
        
        d = Counter(l)
        n = len(d)
        d = sorted(d.items(), key = lambda x : x[1])
        a1 = 0
        a2 = 10**20

        i,j = 0, n-1
        print(d)
        while a1 == 0 or a2 == 10**20:
            if d[i][1] % 2 == 0:
                a2 = min(a2, d[i][1])
            else:
                i += 1
            if d[j][1] % 2 == 1:
                a1 = max(a1, d[j][1])
            else:
                j -= 1
        print(a1,a2)
        return a1-a2
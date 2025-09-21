class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        n = str(n)
        d = collections.defaultdict( lambda : 0)
        l = len(n)

        for x in n:
            d[x] += 1
        d = sorted(d.items(), key = lambda v : (v[1], v[0]))
        return int(d[0][0])

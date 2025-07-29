class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        n = len(ranks)
        # ranks.sort()

        def fun(time):
            c = 0
            for i in range(n):
                x = time//(ranks[i])
                x = math.floor(math.sqrt(x))
                # print(x)
                c += x
            if c >= cars:
                return True
            return False
        l = 0
        # r = max(ranks)*((cars-(n-1))**2)
        r = 10**20
        while l < r:
            m = (l+r)//2
            if fun(m):
                ans = m
                r = m
            else:
                l = m+1
        
        return ans
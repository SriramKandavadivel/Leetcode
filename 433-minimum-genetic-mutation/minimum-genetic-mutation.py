class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        n = len(bank)
        ans = 0
        vis = set()
        # q = deque([startGene])
        q = []
        def push(v):
            heapq.heappush(q,v)
        def pop():
            return heapq.heappop(q)
        push([0,startGene])
        while q:
            
            m = len(q)
            while m > 0:
                ans = pop()
                s = ans[1]
                l = len(s)
                if s == endGene:
                    return ans[0]
                if s not in vis:
                    vis.add(s)
                    for i in range(n):
                        dif = 0
                        b = bank[i]
                        for j in range(l):
                            if s[j] != b[j]:
                                dif += 1
                            if dif > 1:
                                break
                        if dif == 1:
                            x = b
                            if x not in vis:
                                push([ans[0]+1,x])
                m -= 1
        return -1
                        
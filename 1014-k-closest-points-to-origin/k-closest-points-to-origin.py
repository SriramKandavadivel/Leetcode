class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        # d = {}
        h = []
        def push(val):
            heapq.heappush(h,val)
        def pop():
            return heapq.heappop(h)
        
        for x in points:
            dis = sqrt((x[0]-0)**2 + (x[1]-0)**2)
            push([dis,x])
            # d[dis] = x
        ans = []
        for i in range(k):
            ans.append(pop()[1])
        return ans

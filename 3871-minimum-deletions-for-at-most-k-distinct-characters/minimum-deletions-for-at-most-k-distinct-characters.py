class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        # d = collections.defaultdict(lambda : 0)
        l = list(s)
        d = Counter(l)
        op = 0
        
        d = sorted(d.items(), key = lambda v : v[1])
        print(len(d))
        d = deque(d)
        while len(d) > k: 
            v = d.popleft()
            op += v[1]
            print(d)
        return op